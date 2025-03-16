from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate eCommerce dataset
def generate_ecommerce_data(num_records=100):
    data = [{
        "order_id": str(fake.uuid4()),
        "customer_id": str(fake.uuid4()),
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": random.choice(["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Books", "Sports"]),
        "price": round(random.uniform(5, 9999), 2),
        "order_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
        "shipping_date": fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d"),
        "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]),
        "order_status": random.choice(["Processing", "Shipped", "Delivered", "Cancelled", "Returned"]),
        "quantity": random.randint(1, 10),
        "discount": round(random.uniform(0.0, 50.0), 2),
        "shipping_cost": round(random.uniform(0.0, 20.0), 2),
        "total_amount": round(random.uniform(10.0, 10000.0), 2),
        "customer_name": fake.name(),
        "customer_email": fake.email(),
        "delivery_address": fake.address(),
        "tracking_id": fake.bothify(text='??###-#####'),
        "review_rating": random.randint(1, 5),
        "review_comment": fake.sentence(nb_words=12),
        "return_reason": random.choice(["Defective", "Wrong Item", "Size Issue", "Changed Mind", "Other"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_ecommerce_data')
# def download_ecommerce_data():
#     df = generate_ecommerce_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="ecommerce_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
