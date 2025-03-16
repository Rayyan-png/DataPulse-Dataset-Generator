from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Video Data
def generate_video_data(num_records=100):
    data = [{
        "video_id": str(fake.uuid4()),
        "title": fake.sentence(nb_words=6),
        "duration": random.randint(10, 14400),  # 10 secs to 4 hours
        "resolution": random.choice(["480p", "720p", "1080p", "4K", "8K"]),
        "format": random.choice(["MP4", "AVI", "MKV", "MOV", "WMV"]),
        "codec": random.choice(["H.264", "H.265", "VP9", "AV1"]),
        "bitrate": random.randint(500, 50000),  # Bitrate in kbps
        "framerate": random.choice([24, 30, 60, 120]),
        "aspect_ratio": random.choice(["16:9", "4:3", "21:9", "1:1"]),
        "file_size": round(random.uniform(50, 100000), 2),  # Size in MB (50MB to 100GB)
        "category": random.choice(["Education", "Entertainment", "Sports", "Documentary", "Music", "Gaming"]),
        "language": random.choice(["English", "Spanish", "French", "Chinese", "Hindi", "Arabic"]),
        "uploaded_by": fake.name(),
        "upload_date": fake.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d"),
        "license_type": random.choice(["Creative Commons", "Public Domain", "Standard", "Royalty-Free"]),
        "audio_codec": random.choice(["AAC", "MP3", "Opus", "FLAC"]),
        "subtitles": random.choice(["Yes", "No"]),
        "views": random.randint(0, 10000000),
        "likes": random.randint(0, 500000),
        "dislikes": random.randint(0, 50000),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_video_data')
# def download_video_data():
#     df = generate_video_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="video_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_video_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
