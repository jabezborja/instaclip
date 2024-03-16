import os
import json

from openai import OpenAI
from flask import Flask, request, jsonify

from dotenv import load_dotenv
from moviepy.config import change_settings

from utils.video_to_audio import convert_video_to_audio
from utils.audio_to_segments import audio_to_segments
from utils.segments_to_candidates import segments_to_candidates
from utils.candidates_to_video import segment_candidates

load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'io/in'

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

@app.route('/video/upload', methods=['POST'])
def upload_video():

    if not 'file' in request.files:
        return jsonify({"message": "No file part in the request", "success": False}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file", "success": False}), 400
    
    if not file:
        return jsonify({"message": f"File not found", "success": False}), 400

    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    file.save(filepath)

    convert_video_to_audio(filepath, filename)

    return jsonify({
        "message": "File uploaded successfully!",
        "success": True,
        "details": {
            "path": filepath
        }
    }), 200

@app.route('/video/segmentation', methods=['POST'])
def video_segmentation():
    filepath = request.form.get('video_filepath')
    transcription = audio_to_segments(client, filepath)
    segments = jsonify(transcription.segments)

    return segments

@app.route('/video/segment_candidates', methods=['POST'])
def video_segment_candidates():
    segments = request.form.get('segments')
    transcription = segments_to_candidates(client, segments)
    candidates = jsonify(transcription)
    
    return candidates

@app.route('/video/export', methods=['POST'])
def video_export():
    filepath = request.form.get('video_filepath')
    candidates = request.form.get('candidates')
    candidates = json.loads(candidates)

    video_candidates_path = segment_candidates(candidates, filepath, "new_video")

    return jsonify({
        "message": "File exported successfully",
        "success": True,
        "details": {
            "paths": video_candidates_path
        }
    })

if __name__ == '__main__':
    app.run(host=5000)