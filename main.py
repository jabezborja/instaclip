import os
import json

from openai import OpenAI
from flask import Flask, stream_with_context

from dotenv import load_dotenv
from moviepy.config import change_settings

from utils.video_to_audio import convert_video_to_audio
from utils.audio_to_segments import audio_to_segments
from utils.segments_to_filtered import segments_to_filtered
from utils.filtered_to_video import filtered_to_video

load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

@app.route('/video', methods=['POST'])
def main():

    def stream():

        yield "starting"

        convert_video_to_audio('out/video.mp4', 'audio')

        yield "segmenting"

        transcription = audio_to_segments(client)

        yield "identifying"

        transcription = segments_to_filtered(client, transcription)

        yield "exporting"

        filtered_to_video(transcription)

        yield "success"

    return app.response_class(stream(), mimetype='text/plain')

if __name__ == '__main__':
    main()