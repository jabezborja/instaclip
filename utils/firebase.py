import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('env/serviceAccount.json')
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'instaclip-b8df6.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

def upload_file(local_file_path, cloud_file_path):
    bucket = storage.bucket()
    blob = bucket.blob(cloud_file_path)
    blob.upload_from_filename(local_file_path)

    blob.make_public()

    print(f'File {local_file_path} uploaded to {cloud_file_path}.')
    return blob.public_url

def add_data(document_id, collection_name, file_location, additional_data=None):
    db = firestore.client()
    doc_ref = db.collection(collection_name).document(document_id)
    data = {
        'file_location': file_location,
    }
    doc_ref.set(data)

    print(f'Document added to {collection_name} with ID: {document_id}')

def upload_video_to_db(filepath, audiopath):
    video_ref = db.collection("videos").add({})
    video_id = video_ref[1].id

    video_loc = upload_file(filepath, f"videos/{video_id}/video")
    audio_loc = upload_file(audiopath, f"audios/{video_id}/audio")

    doc_ref = db.collection("videos").document(video_id)

    locations ={'video_location': video_loc, 'audio_location': audio_loc }

    doc_ref.update(locations)

    return locations