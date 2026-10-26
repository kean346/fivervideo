from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
out=root/'deliverables/paceIT-editable-final.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=2) as z:
 for folder in ['src','scripts']:
  for p in (root/folder).rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts:z.write(p,'paceIT-project/'+str(p.relative_to(root)))
 for name in ['package.json','package-lock.json','tsconfig.json','.gitignore','README.md','TIMELINE.md','QUALITY-CONTROL.md']:
  z.write(root/name,'paceIT-project/'+name)
 assets=[f'take{i}.mp4' for i in range(1,6)]+['paceit.mp4','flow.mp4','paceit.png','saft.png','northstar.png','flow.png','score.wav','effects.wav']
 for name in assets:z.write(root/'public'/name,'paceIT-project/public/'+name)
 for p in (root/'review').glob('verified*.json'):z.write(p,'paceIT-project/review/'+p.name)
 for name in ['render-qc.json','final-speech-check.json','final-contact-sheet.jpg']:
  z.write(root/'review'/name,'paceIT-project/review/'+name)
 z.write(root/'deliverables/paceIT-captions.srt','paceIT-project/deliverables/paceIT-captions.srt')
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert all(f'paceIT-project/public/take{i}.mp4' in z.namelist() for i in range(1,6))
 print('Final editable archive validated:',out)
