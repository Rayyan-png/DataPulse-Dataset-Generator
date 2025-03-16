from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate transportation data
def generate_transportation_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_time = fake.date_time_this_year()
        arrival_time = fake.date_time_between(start_date=departure_time, end_date="+3d")  # Ensures arrival is after departure

        data.append({
            "transport_id": str(fake.uuid4()),
            "vehicle_type": random.choice(["Car", "Truck", "Bus", "Motorcycle", "Bicycle", "Train"]),
            "route_number": fake.bothify(text="R-###"),
            "departure_city": fake.city(),
            "arrival_city": fake.city(),
            "departure_time": departure_time.strftime("%Y-%m-%d %H:%M:%S"),
            "arrival_time": arrival_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ticket_price": round(random.uniform(5, 500), 2),  # Ticket price in USD
            "driver_name": fake.name(),
            "passenger_count": random.randint(1, 200),
            "transport_status": random.choice(["On Time", "Delayed", "Cancelled"]),
            "fuel_type": random.choice(["Petrol", "Diesel", "Electric", "Hybrid"]),
            "license_plate": fake.license_plate(),
            "transport_company": fake.company(),
            "cargo_type": random.choice(["General", "Perishable", "Hazardous", "Bulk", "Livestock"]),
            "vehicle_capacity": random.randint(1000, 50000),  # Capacity in kg
            "trip_distance": round(random.uniform(10, 2000), 1),  # Distance in km
            "ticket_id": fake.bothify(text="TICKET-####"),
            "logistics_partner": fake.company(),
            "inspection_status": random.choice(["Passed", "Failed", "Pending"]),
        })

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_transportation_data')
# def download_transportation_data():
#     df = generate_transportation_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="transportation_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_transportation_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
