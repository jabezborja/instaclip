import logging

from moviepy.editor import VideoFileClip, concatenate_videoclips

def segment_candidates(candidates, video_file, filename):

    video_candidates_paths = []

    for index, candidate in enumerate(candidates):
        try:
            filename = f"{filename}_{index}"
            out = candidate_to_video(candidate, video_file, filename)
            video_candidates_paths.append(out)
        except Exception as e:
            print(f"Something went wrong on the candidate {e}")

    return video_candidates_paths

def candidate_to_video(transcription, video_file, filename):
    
    clips = []

    for transcribe in transcription["discussion"]:
        start = float(transcribe['start'])
        end = float(transcribe['end'])

        clip = VideoFileClip(video_file).subclip(start, end)

        clips.append(clip)

    height = 420
    aspect_ratio = (9, 16)
    width = int((height / aspect_ratio[1]) * aspect_ratio[0])

    out_path = f"io/out/{filename}.mp4"

    final_clip = concatenate_videoclips(clips).resize(width=width, height=height)
    final_clip.write_videofile(out_path, logger=None)

    for clip in clips:
        clip.close()

    final_clip.close()

    return out_path