import os
import json

from openai import OpenAI

from dotenv import load_dotenv
from moviepy.config import change_settings

from utils.video_to_audio import convert_video_to_audio
from utils.audio_to_segments import audio_to_segments
from utils.segments_to_filtered import segments_to_filtered
from utils.filtered_to_video import filtered_to_video

load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

def main():
    convert_video_to_audio('video.mp4', 'audio')
    transcription = audio_to_segments(client)
    transcription = segments_to_filtered(client, transcription)

    filtered_to_video(transcription)

if __name__ == '__main__':
    main()