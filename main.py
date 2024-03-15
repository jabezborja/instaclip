import os
import json

from openai import OpenAI


from dotenv import load_dotenv
from moviepy.config import change_settings
from moviepy.editor import VideoFileClip, concatenate_videoclips

from utils.video_to_audio import convert_video_to_audio


load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

def main():

    print("Converting Video to Audio...")

    convert_video_to_audio('video.mp4', 'audio')

    print("Listening and transcribing...")

    audio_file= open("audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        response_format='verbose_json',
        file=audio_file
    )
    
    audio_file.close()

    print("Identifying...")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "Identify the best possible good segments to put as a short-form content in the transcription provided by Whisper JSON segments. List down the top 5 best segments with their timestamps that you know there a good context for people watching the short-form content."},
            {"role": "system", "content": "Now, find a great one segment among those five"},
            {"role": "system", "content": "On the best segment that you selected, list down all of the topics"},
            {"role": "system", "content": "Now, choose one best topic"},
            {"role": "system", "content": "Now, get that best topic and create a 30-second short-form content based on the transcription."},
            {"role": "system", "content": "Please return a JSON object where 'discussion' are array of discussion in the best topic on a 30-second short-form content, inside the important array of discussion, there must be a JSON for every discussion, where in there 'text' is the keynote; where 'start' is the video timestamp start; where 'end' is the video timestamp end"},
            {"role": "user", "content": json.dumps(transcription.segments)}
        ]
    )

    print("Producing video for you, please wait...")

    transcription = json.loads(response.choices[0].message.content)

    clips = []

    for index, transcribe in enumerate(transcription["discussion"]):

        print("Iteration #", index)
        
        start = float(transcribe['start'])
        end = float(transcribe['end'])

        clip = VideoFileClip('video.mp4').subclip(start, end)

        clips.append(clip)

    print(clips)

    height = 420
    aspect_ratio = (9, 16)
    width = int((height / aspect_ratio[1]) * aspect_ratio[0])

    print("Exporting video...")

    final_clip = concatenate_videoclips(clips).resize(width=width, height=height)
    final_clip.write_videofile('new_video.mp4')

    for clip in clips:
        clip.close()

    final_clip.close()

if __name__ == '__main__':
    main()