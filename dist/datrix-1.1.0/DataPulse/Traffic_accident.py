from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate traffic accident data
def generate_traffic_accident_data(num_records=100):
    data = []
    for _ in range(num_records):
        num_injuries = random.randint(0, 10)
        num_fatalities = random.randint(0, num_injuries)  # Ensures fatalities ≤ injuries

        data.append({
            "accident_id": str(fake.uuid4()),
            "accident_date": fake.date_this_decade().strftime("%Y-%m-%d"),
            "accident_time": fake.time_object().strftime("%H:%M:%S"),
            "location": fake.address(),
            "vehicle_type": random.choice(["Car", "Truck", "Motorcycle", "Bicycle", "Bus"]),
            "driver_age": random.randint(18, 80),
            "weather_condition": random.choice(["Clear", "Rainy", "Snowy", "Foggy", "Windy"]),
            "cause_of_accident": random.choice(["Speeding", "Distracted Driving", "Drunk Driving", "Weather", "Mechanical Failure"]),
            "injury_severity": random.choice(["None", "Minor", "Moderate", "Severe", "Fatal"]),
            "number_of_vehicles": random.randint(1, 5),
            "number_of_injuries": num_injuries,
            "number_of_fatalities": num_fatalities,
            "accident_description": fake.sentence(),
            "road_type": random.choice(["Highway", "City Road", "Rural Road", "Residential Area"]),
            "police_report_number": fake.bothify("PR###-#####"),
            "hit_and_run": fake.boolean(),
            "alcohol_involved": fake.boolean(),
            "speed_at_time": random.randint(20, 150),  # Speed in km/h
            "damage_estimation": round(random.uniform(100, 50000), 2),  # Damage cost in USD
            "tow_required": fake.boolean()
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_traffic_accident_data')
# def download_traffic_accident_data():
#     df = generate_traffic_accident_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="traffic_accident_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_traffic_accident_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
