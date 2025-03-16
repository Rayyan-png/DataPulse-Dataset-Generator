from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate food supply chain data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        production_date = fake.date_this_decade()
        expiration_date = fake.date_between(start_date=production_date, end_date="+2y")  # Ensures expiration > production

        data.append({
            "product_id": str(fake.uuid4()),  # Ensure UUID is string
            "product_name": f"{fake.word().title()} {fake.word().title()}",
            "supplier": fake.company(),
            "batch_number": fake.bothify("??-#####"),
            "production_date": production_date,
            "expiration_date": expiration_date,
            "quantity": random.randint(10, 1000),
            "storage_temperature": round(random.uniform(0, 30), 1),
            "transport_method": random.choice(["Truck", "Ship", "Airplane", "Train"]),
            "origin_country": fake.country(),
            "destination_country": fake.country(),
            "quality_check": random.choice([True, False]),
            "shipping_cost": round(random.uniform(10, 5000), 2),
            "delivery_status": random.choice(["Pending", "In Transit", "Delivered", "Delayed"]),
            "food_category": random.choice(["Dairy", "Meat", "Vegetables", "Fruits", "Grains", "Beverages"]),
            "packaging_type": random.choice(["Box", "Pallet", "Container", "Bag"]),
            "barcode": fake.ean13(),
            "inspection_date": fake.date_this_year()
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_food_supply_chain_data')
# def download_food_supply_chain_data():
#     df = generate_food_supply_chain_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="food_supply_chain_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_food_supply_chain_data(10)
#     print(sample_df.head(10))  # Print sample data
#     app.run(debug=True)
