import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
timeline=[dict(id=1,fromFrame=0,duration=194,trim=42),dict(id=2,fromFrame=240,duration=240,trim=18),dict(id=3,fromFrame=600,duration=218,trim=25),dict(id=4,fromFrame=1020,duration=225,trim=20),dict(id=5,fromFrame=1410,duration=219,trim=14)]
(root/'src/timeline.json').write_text(json.dumps(timeline,indent=2))
caps=[]
for clip in timeline:
 path=root/f'review/verified{clip["id"]}.json'
 if not path.exists():path=root/f'review/transcript{clip["id"]}.json'
 words=[w for s in json.loads(path.read_text()) for w in s['words']]
 groups=[];n=0
 sizes={1:[3,3,4,5],2:[4,5,4,3,7],3:[5,3,3,3],4:[4,4,4,3,4],5:[6,3,4,5,3]}[clip['id']]
 for count in sizes:
  groups.append(words[n:n+count]);n+=count
 assert n==len(words)
 for g in groups:
  start=max(clip['fromFrame'],clip['fromFrame']+round(g[0]['start']*30)-clip['trim'])
  end=min(clip['fromFrame']+clip['duration'],clip['fromFrame']+round(g[-1]['end']*30)-clip['trim']+3)
  if end<=start:continue
  text=''.join(w['word'] for w in g).strip().replace('PACE IT','paceIT').replace('PACEIT','paceIT').replace('Pace IT','paceIT').replace('pace IT','paceIT').replace('follow ups','follow-ups')
  caps.append(dict(start=start,end=end,text=text))
for a,b in zip(caps,caps[1:]):a['end']=min(a['end'],b['start'])
(root/'src/captions.json').write_text(json.dumps(caps,indent=2))
def timestamp(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(root/'deliverables/paceIT-captions.srt').write_text('\n\n'.join(f'{i+1}\n{timestamp(c["start"])} --> {timestamp(c["end"])}\n{c["text"]}' for i,c in enumerate(caps)))
