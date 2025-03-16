from faker import Faker
import pandas as pd
import random
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_data(num_records=100):
    data = [{
        "sensor_id": fake.uuid4(),
        "air_quality_index": random.randint(0, 500),
        "temperature_celsius": round(random.uniform(-30, 50), 2),
        "humidity_percent": round(random.uniform(0, 100), 2),
        "co2_level_ppm": round(random.uniform(300, 5000), 2),
        "noise_level_db": round(random.uniform(30, 120), 2),
        "rainfall_mm": round(random.uniform(0, 500), 2),
        "wind_speed_kph": round(random.uniform(0, 150), 2),
        "location": fake.city(),
        "country": fake.country(),
        "measurement_date": fake.date_this_decade(),
        "measurement_time": fake.time(),
        "uv_index": round(random.uniform(0, 11), 2),
        "water_quality_index": random.randint(0, 100),
        "pm25": round(random.uniform(0, 500), 2),
        "pm10": round(random.uniform(0, 600), 2),
        "ozone_level_ppb": round(random.uniform(0, 300), 2),
        "so2_level_ppb": round(random.uniform(0, 200), 2),
        "no2_level_ppb": round(random.uniform(0, 400), 2),
        "pollution_source": fake.random_element(elements=["Vehicle Emissions", "Industrial", "Agricultural", "Natural", "Construction"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_environmental_data')
# def download_environmental_data():
#     df = generate_environmental_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
    
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='environmental_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_environmental_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
