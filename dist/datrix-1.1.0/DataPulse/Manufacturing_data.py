from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate manufacturing data
def generate_manufacturing_data(num_records=100):
    data = []
    for _ in range(num_records):
        manufacturing_date = fake.date_between(start_date='-5y', end_date='today')
        expiry_date = fake.date_between(start_date=manufacturing_date, end_date='+5y')  # Ensuring expiry is after manufacturing

        data.append({
            "product_id": str(fake.uuid4()),  # Ensuring UUID is stored as a string
            "product_name": f"{fake.word().capitalize()} {fake.word().capitalize()}",
            "batch_number": fake.bothify(text="BATCH-####"),
            "manufacturing_date": manufacturing_date.strftime("%Y-%m-%d"),
            "expiry_date": expiry_date.strftime("%Y-%m-%d"),
            "factory_location": fake.city(),
            "machine_id": fake.bothify(text="M-###"),
            "worker_id": fake.random_int(min=100000, max=999999),
            "quality_check_status": random.choice(["Passed", "Failed", "Pending"]),
            "material_used": random.choice(["Steel", "Plastic", "Aluminum", "Wood", "Rubber"]),
            "production_cost": round(random.uniform(100.00, 9999.99), 2),
            "output_quantity": random.randint(100, 10000),
            "defect_rate": round(random.uniform(0.001, 0.099), 3),
            "shift": random.choice(["Day", "Night"]),
            "supervisor_name": fake.name(),
            "power_consumption": round(random.uniform(50.00, 500.00), 2),
            "production_line": fake.bothify(text="Line-##"),
            "storage_condition": random.choice(["Cool", "Dry", "Ambient"]),
            "shipping_status": random.choice(["Ready", "In Transit", "Delayed"]),
            "equipment_used": random.choice(["CNC Machine", "Conveyor Belt", "Injection Molder", "Lathe", "Press"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_manufacturing_data')
# def download_manufacturing_data():
#     df = generate_manufacturing_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="manufacturing_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_manufacturing_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
