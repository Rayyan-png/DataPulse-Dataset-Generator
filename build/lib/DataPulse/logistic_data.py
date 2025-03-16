from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate logistics data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_date = fake.date_between(start_date='-1y', end_date='today')
        arrival_date = fake.date_between(start_date=departure_date, end_date='+1y')  # Ensuring arrival is after departure

        data.append({
            "shipment_id": str(fake.uuid4()),  # Ensuring UUID is stored as a string
            "origin": fake.city(),
            "destination": fake.city(),
            "departure_date": departure_date.strftime("%Y-%m-%d"),
            "arrival_date": arrival_date.strftime("%Y-%m-%d"),
            "transport_mode": random.choice(["Air", "Sea", "Road", "Rail"]),
            "carrier_name": fake.company(),
            "tracking_number": fake.bothify(text="??-########"),
            "package_weight": round(random.uniform(1.00, 99.99), 2),  # Avoiding too small values
            "package_volume": round(random.uniform(10.00, 999.99), 2),
            "status": random.choice(["In Transit", "Delivered", "Pending", "Cancelled"]),
            "customer_name": fake.name(),
            "contact_number": fake.phone_number(),
            "shipping_cost": round(random.uniform(100.00, 9999.99), 2),
            "priority_level": random.choice(["Standard", "Express", "Overnight"]),
            "vehicle_id": fake.bothify(text="???-####"),
            "driver_name": fake.name(),
            "delivery_address": fake.address(),
            "customs_clearance_status": random.choice(["Cleared", "Pending", "Held"]),
            "insurance_coverage": round(random.uniform(1000.00, 99999.99), 2),
        })

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_logistics_data')
# def download_logistics_data():
#     df = generate_logistics_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="logistics_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_logistics_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
