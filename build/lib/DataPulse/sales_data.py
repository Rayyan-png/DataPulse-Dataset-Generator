from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate sales data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        quantity = random.randint(1, 100)
        unit_price = round(random.uniform(1, 9999), 2)
        total_amount = round(quantity * unit_price, 2)

        data.append({
            "sale_id": str(fake.uuid4()),
            "product_name": fake.word().title(),
            "customer_id": str(fake.uuid4()),
            "sale_date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount,
            "discount": round(random.uniform(0, 99), 2),
            "payment_method": random.choice(["Credit Card", "Debit Card", "Cash", "Bank Transfer"]),
            "salesperson": fake.name(),
            "region": fake.state(),
            "country": fake.country(),
            "invoice_number": fake.bothify("INV###-###"),
            "customer_type": random.choice(["Retail", "Wholesale", "Online"]),
            "return_status": random.choice(["No Return", "Partial Return", "Full Return"]),
            "shipping_method": random.choice(["Standard", "Express", "Overnight"]),
            "delivery_status": random.choice(["Delivered", "Pending", "Cancelled"]),
            "product_category": random.choice(["Electronics", "Clothing", "Home Appliances", "Books", "Beauty"]),
            "loyalty_points": random.randint(0, 1000),
            "channel": random.choice(["Online", "In-Store", "Phone"]),
        })

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_sales_data')
# def download_sales_data():
#     df = generate_sales_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="sales_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_sales_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
