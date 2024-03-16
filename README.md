# Instaclip: AI Short-Form Video Content Generator

Instaclip leverages cutting-edge AI technology, including OpenAI's Whisper for automatic transcription and GPT-3 for content analysis, alongside MoviePy for video editing, to transform long videos into captivating short-form content.

![image](https://github.com/jabezborja/instaclip/assets/64759159/36877542-c6d8-4347-b762-d5e06b4adf9c)

Designed for creators aiming to enhance their presence on platforms like Instagram Reels and TikTok, Instaclip automates the selection and editing process, making content creation effortless and accessible.

## Features
* Whisper Integration: Utilizes OpenAI's Whisper to accurately transcribe audio, enabling the AI to understand and select key moments based on both video and audio content.
* GPT-3 Content Analysis: Employs GPT-3 to analyze transcriptions and identify the most engaging segments, ensuring the clips resonate with audiences.
* MoviePy Editing: Leverages MoviePy for efficient video editing, providing high-quality, customizable short-form videos.
* Customizable Lengths: Supports generation of videos tailored to the specific requirements of different social media platforms.
* Batch Processing: Offers the ability to process multiple videos simultaneously, streamlining content creation.

## Installation

### Prerequisites
* Python 3.8 or higher
* FFmpeg
* An OpenAI API key for Whisper and GPT-3

### Steps
* Clone the Instaclip repository:

```bash
git clone https://github.com/jabezborja/instaclip.git
```

* Navigate to the Instaclip directory:
```bash
cd instaclip
```

* Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Before running Instaclip, ensure you have set your OpenAI API key in your `.env`:
```bash
OPENAI_API_KEY='your_api_key_here'
```

To convert a long video into short-form content, follow these steps:

Launch Instaclip:
```
flask --app main run
```

*Note: The frontend is still implementing so you can use the API endpoint with POSTMAN for now.*

To generate a short-form content. You must call

```
/video/upload -> uploads the videos and turns it into listenable mp3 for Whisper
/video/segmentation -> you pass the video_filepath from /video/upload, this returns segmented and processed transcription
/video/segment_candidates -> you pass the processed segmented and transcription, this returns the video candidates - best possible content
/video/export -> you pass the video_filepath and candidates, this returns the output path of the videos, this is now the short-form content generated.
```

## Contributing
We welcome contributions to Instaclip. To contribute, please follow these guidelines:

* Fork the repository.
* Create a new branch for your feature (git checkout -b feature/AmazingFeature).
* Commit your changes (git commit -m 'Add some AmazingFeature').
* Push to the branch (git push origin feature/AmazingFeature).
* Open a pull request.

## License

Instaclip is licensed under the GNU Affero General Public License (AGPL). This means that if you use the software (or any part of it) to interact with users over a network, you must provide the source code under this license.

See the LICENSE file in the repository for the full license text.
