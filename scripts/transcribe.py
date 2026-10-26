"""Run after Hugging Face model access is enabled. Review generated words before publication."""
import json, wave
import numpy as np
from pathlib import Path
from faster_whisper import WhisperModel
root=Path(__file__).resolve().parents[1]
model=WhisperModel('small.en',device='cpu',compute_type='int8',cpu_threads=4,download_root=str(root/'model-cache'))
offsets=[0,242,600,1010,1380]
captions=[]
for i,offset in enumerate(offsets,1):
 with wave.open(str(root/f'review/camera{i}.wav')) as w:
  samples=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
 segments,_=model.transcribe(samples,word_timestamps=True,language='en',initial_prompt='Kean, paceIT. Professional business websites, custom dashboards, quotations, workflow automation.')
 transcript=[]
 for seg in segments:
  transcript.append({'start':seg.start,'end':seg.end,'text':seg.text,'words':[{'start':w.start,'end':w.end,'word':w.word} for w in seg.words]})
  for n in range(0,len(seg.words),6):
   ws=seg.words[n:n+6]
   captions.append({'start':offset+round(ws[0].start*30),'end':offset+round(ws[-1].end*30),'text':''.join(w.word for w in ws).strip()})
 (root/f'review/transcript{i}.json').write_text(json.dumps(transcript,indent=2))
(root/'src/captions.json').write_text(json.dumps(captions,indent=2))
print('Draft captions written. Verify transcription and timing before final rendering.')
