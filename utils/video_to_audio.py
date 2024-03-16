import os

from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_file, audio_file_name, output_ext="mp3"):

    out = f"io/out/{audio_file_name}.{output_ext}"

    clip = VideoFileClip(video_file)
    clip = clip.set_end(150)
    clip.audio.write_audiofile(out)

    return out