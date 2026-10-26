# Final quality-control report

## Completed outputs

- `paceIT-1080p.mp4`: 1920×1080, H.264 video, AAC audio, 30 fps.
- `paceIT-preview-final.mp4`: 960×540, same complete edit and audio.
- Both files: 1740 video frames, 58.000 seconds of video; 58.005 seconds container duration due to AAC packet padding.
- Both files passed full FFmpeg decoding without errors.
- Final mix: −16.78 LUFS integrated, −1.44 dBTP true peak, 8.40 LU loudness range. No measured clipping.
- 23 phrase captions: valid timeline boundaries and no overlapping subtitle intervals. SRT and editable frame-timed JSON are supplied.
- TypeScript checking passed; Remotion rendered both complete outputs successfully.

## Source and editorial checks

All five founder clips remain in the latest supplied order. Only quiet clip beginnings/endings were shortened; no spoken sentence was deliberately removed or reordered. The four original PNGs from the supplied ZIP are used, replacing the draft's low-resolution crops. Original MOVs remain untouched in the workspace.

Whisper small.en and medium.en were used to check source speech, word timings, and captions. The medium model resolved “a smarter process.” The exported final mix was transcribed again by medium.en by camera section; all five introductions/explanations/closing passages were present. Clip 2's final-mix recognition varied between “I've got experiences” and the two source recognizers' “I build experiences”; captions retain the source-model agreement. Automatic recognition is not a human listening certification.

Rendered full-resolution stills were inspected at the captioned introduction, gesture/screen transition, SAFT screen, Flow/Northstar showcase, workflow demonstration and closing card. A contact sheet from the actual final 1080p MP4 was also inspected across the timeline. The face remains clear of overlays, captions fit within safe margins, and portfolio labels/end-card text remain on screen.

## Portfolio accuracy

- Flow Plumbing and Northstar are labelled demonstrations with fictional data.
- Enquiry/quotation/follow-up automation is labelled illustrative. No delivered integration or customer result is claimed.
- Moving footage comes from the supplied paceIT website walkthrough and Flow demonstration.
- SA Family Travel uses the supplied original screenshot and its appearance in the real paceIT walkthrough. A dedicated SAFT screen recording was not supplied and has not been fabricated.
- Northstar uses the real supplied dashboard image; its displayed metrics are not altered or presented as paceIT business results.
- No external contact details or off-platform invitation are added. The closing call to action is “Message me on Fiverr to discuss your project.”

## Audio and motion

Original founder audio is preserved with high-pass filtering, conservative denoising and loudness processing. The music bed and subtle transition sounds are original synthesized assets produced by included scripts. No generated founder voice or third-party music recording is used.

Gesture reveals and the hand-sweep screen change use manually synchronized keyframes; they are not automatic motion tracking. Camera footage has restrained digital push-ins and consistent mild colour correction. Exact edit decisions and keyframe times are in `TIMELINE.md`.

## Scope of verification

Visual sampling, full decoding, numerical audio analysis, source transcription comparison and final-mix speech recognition were performed. This does not constitute a human real-time listening session or Fiverr platform approval. Download delivery depends on the host application's file-link support; local file integrity is verified independently. SHA-256 checksums and detailed measurements are in `review/render-qc.json`.
