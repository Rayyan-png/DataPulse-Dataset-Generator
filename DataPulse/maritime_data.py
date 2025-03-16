from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate maritime data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_date = fake.date_between(start_date='-1y', end_date='today')
        arrival_date = fake.date_between(start_date=departure_date, end_date='today')  # Ensuring arrival is after departure

        data.append({
            "ship_id": str(fake.uuid4()),  # Ensuring UUID is stored as a string
            "ship_name": fake.company(),
            "departure_port": fake.city(),
            "arrival_port": fake.city(),
            "departure_date": departure_date.strftime("%Y-%m-%d"),
            "arrival_date": arrival_date.strftime("%Y-%m-%d"),
            "cargo_type": random.choice(["Containers", "Oil", "Gas", "Automobiles", "Electronics", "Food Products"]),
            "ship_type": random.choice(["Cargo", "Tanker", "Cruise", "Fishing", "Naval"]),
            "weight_tons": round(random.uniform(100.00, 100000.00), 2),
            "crew_size": random.randint(10, 100),
            "vessel_flag": fake.country_code(),
            "shipping_company": fake.company(),
            "speed_knots": random.randint(10, 40),
            "navigation_status": random.choice(["Underway", "Anchored", "Moored", "Docked"]),
            "incident_reported": fake.boolean(),
            "ship_registration_number": fake.bothify("SHIP-###-????"),
            "latitude": round(fake.latitude(), 6),
            "longitude": round(fake.longitude(), 6),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_maritime_data')
# def download_maritime_data():
#     df = generate_maritime_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="maritime_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_maritime_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
