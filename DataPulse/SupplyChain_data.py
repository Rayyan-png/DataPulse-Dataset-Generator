from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate supply chain data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        quantity = random.randint(1, 1000)
        unit_price = round(random.uniform(5, 500), 2)
        total_cost = round(quantity * unit_price, 2)  # Ensure accurate total cost

        data.append({
            "order_id": str(fake.uuid4()),
            "product_name": fake.word(),
            "supplier_name": fake.company(),
            "order_date": fake.date_this_year().strftime("%Y-%m-%d"),
            "delivery_date": fake.date_between(start_date='today', end_date='+30d').strftime("%Y-%m-%d"),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_cost": total_cost,
            "order_status": random.choice(["Pending", "Shipped", "Delivered", "Cancelled"]),
            "warehouse_location": fake.city(),
            "transport_mode": random.choice(["Air", "Sea", "Rail", "Road"]),
            "tracking_number": fake.bothify(text="??###-####"),
            "inventory_level": random.randint(0, 10000),
            "return_status": random.choice(["No Return", "In Process", "Completed"]),
            "dispatch_center": fake.city(),
            "shipping_cost": round(random.uniform(5, 200), 2),
            "order_priority": random.choice(["High", "Medium", "Low"]),
            "supplier_contact": fake.phone_number(),
            "carrier_name": fake.company(),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_supply_chain_data')
# def download_supply_chain_data():
#     df = generate_supply_chain_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="supply_chain_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_supply_chain_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
