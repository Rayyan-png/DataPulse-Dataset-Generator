from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate real estate data
def generate_real_estate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "property_id": str(fake.uuid4()),
            "listing_price": round(random.uniform(50000, 5000000), 2),
            "property_type": random.choice(["Apartment", "House", "Condo", "Villa", "Townhouse"]),
            "address": fake.address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "country": fake.country(),
            "bedrooms": random.randint(1, 10),
            "bathrooms": random.randint(1, 8),
            "square_feet": random.randint(500, 10000),
            "listing_date": fake.date_this_year().strftime("%Y-%m-%d"),
            "sale_status": random.choice(["Available", "Pending", "Sold"]),
            "agent_name": fake.name(),
            "agent_phone": fake.phone_number(),
            "year_built": random.randint(1900, 2023),
            "parking_spaces": random.randint(0, 5),
            "property_tax": round(random.uniform(1000, 50000), 2),
            "listing_description": fake.sentence(nb_words=15),
            "hoa_fee": round(random.uniform(50, 5000), 2),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_real_estate_data')
# def download_real_estate_data():
#     df = generate_real_estate_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="real_estate_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_real_estate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
