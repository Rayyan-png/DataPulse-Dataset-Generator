from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_audio_id():
    return str(fake.uuid4())  # Ensure UUID is a string

def generate_title():
    return fake.sentence(nb_words=5)

def generate_duration():
    return random.randint(30, 7200)  # Duration in seconds (30 secs to 2 hours)

def generate_bitrate():
    return random.randint(64, 320)  # Bitrate in kbps

def generate_sample_rate():
    return random.choice([44100, 48000, 96000])  # Sample rate in Hz

def generate_format():
    return random.choice(["MP3", "WAV", "FLAC", "AAC", "OGG"])

def generate_codec():
    return random.choice(["AAC", "MP3", "Opus", "FLAC", "Vorbis"])

def generate_file_size():
    return round(random.uniform(1.0, 500.0), 2)  # Size in MB (1MB - 500MB)

def generate_artist():
    return fake.name()

def generate_album():
    return fake.sentence(nb_words=3)

def generate_genre():
    return random.choice(["Pop", "Rock", "Jazz", "Classical", "Hip-Hop", "Electronic"])

def generate_release_date():
    return fake.date_between(start_date='-10y', end_date='today')

def generate_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese", "Japanese"])

def generate_license_type():
    return random.choice(["Creative Commons", "Public Domain", "Standard", "Royalty-Free"])

def generate_publisher():
    return fake.company()

def generate_explicit_content():
    return random.choice([True, False])

def generate_channels():
    return random.choice(["Mono", "Stereo", "Surround 5.1", "Surround 7.1"])

def generate_mood():
    return random.choice(["Happy", "Sad", "Relaxing", "Energetic", "Romantic", "Dramatic"])

def generate_listens():
    return random.randint(0, 1000000)

def generate_likes():
    return random.randint(0, 500000)

def generate_dislikes():
    return random.randint(0, 50000)

def generate_data(num_records=100):
    data = [
        {
            "audio_id": generate_audio_id(),
            "title": generate_title(),
            "duration": generate_duration(),
            "bitrate": generate_bitrate(),
            "sample_rate": generate_sample_rate(),
            "format": generate_format(),
            "codec": generate_codec(),
            "file_size": generate_file_size(),
            "artist": generate_artist(),
            "album": generate_album(),
            "genre": generate_genre(),
            "release_date": generate_release_date(),
            "language": generate_language(),
            "license_type": generate_license_type(),
            "publisher": generate_publisher(),
            "explicit_content": generate_explicit_content(),
            "channels": generate_channels(),
            "mood": generate_mood(),
            "listens": generate_listens(),
            "likes": generate_likes(),
            "dislikes": generate_dislikes(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Display sample DataFrame
df_sample = generate_data(10)
print(df_sample.head())

# Flask app to download large datasets
# from flask import Flask, send_file

# app = Flask(__name__)

# @app.route('/download_audio_data')
# def download_audio_data():
#     df = generate_audio_data(500000)
#     file_path = "audio_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
