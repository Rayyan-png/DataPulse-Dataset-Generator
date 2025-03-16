from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate IoT data
def generate_iot_data(num_records=100):
    data = []
    for _ in range(num_records):
        last_active = fake.date_time_this_year()

        data.append({
            "device_id": str(fake.uuid4()),  # Ensure UUID is a string
            "device_type": random.choice(["Sensor", "Smart Light", "Smart Thermostat", "Smart Camera", "Wearable", "Smart Plug"]),
            "temperature": round(random.uniform(-30, 50), 2),  # Direct random range for efficiency
            "humidity": round(random.uniform(0, 100), 2),
            "battery_level": random.randint(0, 100),
            "signal_strength": random.randint(-100, -30),
            "firmware_version": fake.bothify(text="v?.##"),
            "location": fake.city(),
            "connection_status": random.choice(["Online", "Offline", "Error"]),
            "last_active": last_active.strftime("%Y-%m-%d %H:%M:%S"),  # Proper date format
            "data_rate": round(random.uniform(0.1, 9.9999), 4),
            "ip_address": fake.ipv4(),
            "mac_address": fake.mac_address(),
            "power_consumption": round(random.uniform(0.01, 99.999), 3),  # Reasonable power values
            "alert_status": random.choice(["Normal", "Warning", "Critical"]),
            "uptime_hours": random.randint(0, 8760),
            "device_owner": fake.name(),
            "network_type": random.choice(["WiFi", "Ethernet", "Cellular"]),
            "data_packet_size": random.randint(64, 1500),
            "device_model": fake.bothify(text="Model-###"),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_iot_data')
# def download_iot_data():
#     df = generate_iot_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="iot_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_iot_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
