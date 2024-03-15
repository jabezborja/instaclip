
def audio_to_segments(client):
    
    audio_file= open("out/audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        response_format='verbose_json',
        file=audio_file
    )
    
    audio_file.close()

    return transcription