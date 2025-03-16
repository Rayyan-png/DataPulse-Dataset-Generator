from faker import Faker
import pandas as pd
import random
import io
import json
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Image Metadata
def generate_image_data(num_records=100):
    data = []
    for _ in range(num_records):
        capture_date = fake.date_between(start_date='-5y', end_date='today')

        data.append({
            "image_id": str(fake.uuid4()),  # Ensure UUID is a string
            "image_url": fake.image_url(),
            "image_format": random.choice(["JPEG", "PNG", "BMP", "GIF", "TIFF"]),
            "resolution": f"{random.randint(640, 3840)}x{random.randint(480, 2160)}",
            "file_size": f"{random.randint(100, 5000)} KB",
            "color_mode": random.choice(["RGB", "CMYK", "Grayscale", "RGBA"]),
            "capture_device": random.choice(["DSLR", "Smartphone", "Drone", "Webcam", "Security Camera"]),
            "location": fake.city(),
            "capture_date": capture_date.strftime("%Y-%m-%d"),
            "license_type": random.choice(["Public Domain", "Creative Commons", "Royalty-Free", "Editorial Use Only"]),
            "alt_text": fake.sentence(),
            "image_category": random.choice(["Nature", "Urban", "Portrait", "Abstract", "Food", "Sports", "Technology"]),
            "aspect_ratio": random.choice(["16:9", "4:3", "1:1", "3:2", "21:9"]),
            "metadata": json.dumps({
                "ISO": random.randint(100, 3200),
                "Aperture": f"f/{random.randint(1, 22)}",
                "Shutter Speed": f"1/{random.randint(30, 8000)}s"
            }),  # Store as JSON string
            "photographer": fake.name(),
            "watermark": random.choice([True, False]),
            "image_tags": json.dumps([fake.word() for _ in range(5)]),  # Store as JSON string
            "image_source": random.choice(["Stock Library", "User Upload", "Generated", "Archived"]),
            "focal_length": f"{random.randint(18, 200)}mm",
            "image_orientation": random.choice(["Landscape", "Portrait", "Square"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_image_data')
# def download_image_data():
#     df = generate_image_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="image_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_image_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
