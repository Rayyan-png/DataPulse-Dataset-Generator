from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Weather Data
def generate_data(num_records=100):
    data = [{
        "station_id": str(fake.uuid4()),
        "station_name": f"{fake.city()} Weather Station",
        "temperature": round(random.uniform(-30, 50), 1),
        "humidity": random.randint(10, 100),
        "wind_speed": round(random.uniform(0, 50), 1),
        "wind_direction": random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"]),
        "precipitation": round(random.uniform(0, 300), 1),
        "pressure": round(random.uniform(900, 1100), 1),
        "visibility": round(random.uniform(0, 50), 1),
        "cloud_cover": random.randint(0, 100),
        "weather_condition": random.choice(["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Foggy", "Windy"]),
        "recorded_at": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
        "uv_index": random.randint(0, 11),
        "air_quality_index": random.randint(0, 500),
        "dew_point": round(random.uniform(-20, 30), 1),
        "solar_radiation": round(random.uniform(0, 1500), 1),
        "fog_density": round(random.uniform(0, 1), 2),
        "rainfall_probability": random.randint(0, 100),
        "snow_depth": round(random.uniform(0, 100), 1),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_weather_data')
# def download_weather_data():
#     df = generate_weather_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="weather_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_weather_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
