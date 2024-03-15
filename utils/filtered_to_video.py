from moviepy.editor import VideoFileClip, concatenate_videoclips

def filtered_to_video(transcription, video_file, filename):
    
    clips = []

    for index, transcribe in enumerate(transcription["discussion"]):
        
        start = float(transcribe['start'])
        end = float(transcribe['end'])

        clip = VideoFileClip(video_file).subclip(start, end)

        clips.append(clip)

        print("Iterating at", index)

    height = 420
    aspect_ratio = (9, 16)
    width = int((height / aspect_ratio[1]) * aspect_ratio[0])

    out_path = f"io/out/{filename}.mp4"

    final_clip = concatenate_videoclips(clips).resize(width=width, height=height)
    final_clip.write_videofile(out_path)

    for clip in clips:
        clip.close()

    final_clip.close()

    return out_path