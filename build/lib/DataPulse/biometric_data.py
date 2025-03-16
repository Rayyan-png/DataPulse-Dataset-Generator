from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker and Flask
fake = Faker()
app = Flask(__name__)

# Function to generate biometric data
def generate_data(num_records=100):
    data = [{
        "user_id": str(fake.uuid4()),
        "fingerprint_hash": fake.sha256(),
        "face_id": fake.sha256(),
        "iris_scan": fake.sha256(),
        "voice_sample": random.choice(["Male", "Female", "Neutral"]),
        "hand_geometry": fake.sha256(),
        "retina_scan": fake.sha256(),
        "signature_pattern": fake.sha256(),
        "dna_sequence": fake.sha256(),
        "gait_pattern": fake.sha256(),
        "keystroke_dynamics": fake.sha256(),
        "palm_vein_pattern": fake.sha256(),
        "ear_shape": random.choice(["Round", "Oval", "Pointed"]),
        "skin_texture": random.choice(["Smooth", "Rough", "Scarred"]),
        "facial_landmarks": random.choice(["High Cheekbones", "Wide Jaw", "Pointed Chin"]),
        "voice_pitch": round(random.uniform(50, 300), 2),
        "eye_color": random.choice(["Brown", "Blue", "Green", "Hazel", "Gray"]),
        "body_temperature": round(random.uniform(35, 42), 1),
        "heart_rate": random.randint(60, 100),
        "blood_pressure": f"{random.randint(90, 140)}/{random.randint(60, 90)}"
    } for _ in range(num_records)]
    
    return pd.DataFrame(data)

# Flask API endpoint for downloading biometric data
# @app.route('/download_biometric_data')
# def download_biometric_data():
#     df = generate_biometric_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="biometric_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
