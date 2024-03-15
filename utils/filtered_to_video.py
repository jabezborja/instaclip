from moviepy.editor import VideoFileClip, concatenate_videoclips

def filtered_to_video(transcription):
    
    clips = []

    for index, transcribe in enumerate(transcription["discussion"]):

        print("Iteration #", index)
        
        start = float(transcribe['start'])
        end = float(transcribe['end'])

        clip = VideoFileClip('video.mp4').subclip(start, end)

        clips.append(clip)

    height = 420
    aspect_ratio = (9, 16)
    width = int((height / aspect_ratio[1]) * aspect_ratio[0])

    final_clip = concatenate_videoclips(clips).resize(width=width, height=height)
    final_clip.write_videofile('new_video.mp4')

    for clip in clips:
        clip.close()

    final_clip.close()