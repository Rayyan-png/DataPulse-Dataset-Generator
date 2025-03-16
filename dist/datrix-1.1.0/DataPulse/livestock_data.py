from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate livestock data
def generate_livestock_data(num_records=100):
    data = []
    for _ in range(num_records):
        birth_date = fake.date_of_birth(minimum_age=0, maximum_age=10)
        checkup_date = fake.date_this_year()

        data.append({
            "animal_id": str(fake.uuid4()),  # Ensuring UUID is stored as a string
            "species": random.choice(["Cattle", "Sheep", "Goat", "Pig", "Chicken", "Horse"]),
            "breed": fake.word().title() + " Breed",
            "birth_date": birth_date.strftime("%Y-%m-%d"),
            "weight": round(random.uniform(10.00, 1500.00), 2),  # More realistic weight range
            "health_status": random.choice(["Healthy", "Sick", "Recovered", "Under Observation"]),
            "farm_location": f"{fake.city()}, {fake.country()}",
            "owner_name": fake.name(),
            "feed_type": random.choice(["Grass", "Grain", "Silage", "Mixed Feed"]),
            "veterinary_checkup_date": checkup_date.strftime("%Y-%m-%d"),
            "milk_production": round(random.uniform(0.0, 50.0), 1),  # Milk production in liters
            "reproductive_status": random.choice(["Pregnant", "Lactating", "Neutered", "Fertile"]),
            "tag_number": fake.bothify("TAG-###-????"),
            "vaccination_status": random.choice(["Up-to-date", "Pending", "Overdue"]),
            "transportation_method": random.choice(["Truck", "Train", "Air", "Ship"]),
            "destination": f"{fake.city()}, {fake.country()}",
            "inspection_result": random.choice(["Passed", "Failed", "Pending"]),
            "sales_price": round(random.uniform(50.00, 10000.00), 2),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_livestock_data')
# def download_livestock_data():
#     df = generate_livestock_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="livestock_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_livestock_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
