from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate customer dataset
def generate_data(num_records=100):
    data = [{
        "customer_id": str(fake.uuid4()),
        "customer_name": fake.name(),
        "age": random.randint(18, 90),
        "gender": random.choice(["Male", "Female", "Other"]),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address(),
        "city": fake.city(),
        "state": fake.state(),
        "country": fake.country(),
        "postal_code": fake.postcode(),
        "registration_date": fake.date_this_decade(),
        "last_purchase_date": fake.date_between(start_date="-1y", end_date="today"),
        "loyalty_points": random.randint(0, 10000),
        "preferred_payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]),
        "customer_segment": random.choice(["Regular", "VIP", "Wholesale", "Online-Only"]),
        "subscription_status": random.choice(["Active", "Inactive", "Cancelled"]),
        "total_spent": round(random.uniform(100.00, 1000000.00), 2),
        "feedback_score": random.randint(1, 5),
        "referral_source": random.choice(["Social Media", "Friend", "Advertisement", "Search Engine"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_customer_data')
# def download_customer_data():
#     df = generate_customer_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="customer_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
