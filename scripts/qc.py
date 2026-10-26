from pathlib import Path
import subprocess,json,hashlib
root=Path(__file__).resolve().parents[1]
results=[]
for name in ['paceIT-preview-final.mp4','paceIT-1080p.mp4']:
 p=root/'deliverables'/name
 d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
 v=next(s for s in d['streams'] if s['codec_type']=='video');a=next(s for s in d['streams'] if s['codec_type']=='audio')
 assert v['codec_name']=='h264' and a['codec_name']=='aac'
 assert v['r_frame_rate']=='30/1'
 assert 55<=float(d['format']['duration'])<=59
 assert int(v['nb_frames'])==1740
 if '1080p' in name:assert (v['width'],v['height'])==(1920,1080)
 run=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-16:TP=-1.5:LRA=9:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
 text=run.stderr;metrics=json.JSONDecoder().raw_decode(text[text.rfind('{'):])[0]
 assert float(metrics['input_tp'])<0
 results.append({'file':name,'duration':d['format']['duration'],'frames':v['nb_frames'],'resolution':[v['width'],v['height']],'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'audio_measurements':metrics,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'full_decode':'passed'})
(root/'review/render-qc.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
