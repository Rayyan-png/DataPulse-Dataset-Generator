from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate retail data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "product_id": str(fake.uuid4()),
            "product_name": fake.word().title() + " " + fake.word().title(),
            "category": random.choice(["Electronics", "Clothing", "Home & Garden", "Toys", "Groceries", "Beauty"]),
            "price": round(random.uniform(10, 999), 2),
            "discount": round(random.uniform(0, 99), 2),
            "stock_quantity": random.randint(0, 1000),
            "supplier": fake.company(),
            "brand": fake.company_suffix(),
            "sku": fake.bothify(text='??-#####'),
            "store_location": fake.city(),
            "sale_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "customer_id": str(fake.uuid4()),
            "payment_method": random.choice(["Credit Card", "Debit Card", "Cash", "Online Payment"]),
            "return_status": random.choice(["Not Returned", "Returned", "Exchange"]),
            "review_score": random.randint(1, 5),
            "shipping_cost": round(random.uniform(5, 50), 2),
            "tax_amount": round(random.uniform(1, 30), 2),
            "delivery_status": random.choice(["Delivered", "In Transit", "Pending", "Cancelled"]),
            "warranty_period": random.choice(["6 months", "1 year", "2 years", "No Warranty"]),
            "sales_channel": random.choice(["Online", "In-Store", "Wholesale"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_retail_data')
# def download_retail_data():
#     df = generate_retail_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="retail_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_retail_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
