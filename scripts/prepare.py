import subprocess, json, numpy as np, wave
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for i in range(1,6):
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(root/f'public/camera{i}.mov'),'-vf','scale=1920:1080,fps=30,eq=contrast=1.025:saturation=0.96','-af','highpass=f=80,afftdn=nf=-25,loudnorm=I=-16:TP=-1.5:LRA=9','-c:v','libx264','-preset','fast','-crf','18','-threads','2','-c:a','aac','-b:a','192k','-movflags','+faststart',str(root/f'public/take{i}.mp4')],check=True)
 print('Prepared',i,flush=True)
# Original, synthesized ambient score: no third-party recording or licensing dependency.
sr=48000; duration=58; t=np.arange(sr*duration)/sr; music=np.zeros_like(t)
chords=[(130.81,164.81,196,246.94),(110,130.81,164.81,196),(87.31,130.81,174.61,220),(98,146.83,196,246.94)]
for start in np.arange(0,duration,4):
 local=t-start; active=(local>=0)&(local<5)
 env=np.clip(local/0.7,0,1)*np.clip((5-local)/1.5,0,1)*active
 for f in chords[int(start/4)%4]:music+=0.012*np.sin(2*np.pi*f*t)*env
for start in np.arange(0,duration,0.5):
 local=t-start; env=np.exp(-np.maximum(local,0)*14)*(local>=0)*(local<0.4)
 f=[523.25,659.25,783.99,987.77][int(start*2)%4]
 music+=0.008*np.sin(2*np.pi*f*t)*env
music*=np.minimum(t/2,1)*np.clip((duration-t)/2,0,1)
with wave.open(str(root/'public/score.wav'),'w') as w:
 w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((music*32767).astype('<i2').tobytes())
