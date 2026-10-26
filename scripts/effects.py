from pathlib import Path
import numpy as np,wave
root=Path(__file__).resolve().parents[1]
sr=48000;y=np.zeros(58*sr);rng=np.random.default_rng(13)
for sec in [9.8333,11.6333,21,25.6667,27.2667,41.5,54.3]:
 n=int(.3*sr);t=np.arange(n)/sr
 noise=rng.normal(0,1,n);noise=np.convolve(noise,np.ones(24)/24,mode='same')
 pulse=.025*noise*np.sin(np.pi*t/.3)**2+.008*np.sin(2*np.pi*(660*t-450*t*t))*np.exp(-t*22)
 a=int(sec*sr);y[a:a+n]+=pulse
with wave.open(str(root/'public/effects.wav'),'w') as w:
 w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((y*32767).astype('<i2').tobytes())
