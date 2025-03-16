from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Insurance Data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        policy_start_date = fake.date_between(start_date='-5y', end_date='today')
        policy_end_date = fake.date_between(start_date='today', end_date='+5y')
        claim_date = fake.date_between(start_date='-3y', end_date='today')

        data.append({
            "policy_id": str(fake.uuid4()),  # Ensure UUID is a string
            "policy_holder_name": fake.name(),
            "policy_type": random.choice(["Health", "Auto", "Home", "Life", "Travel", "Business"]),
            "premium_amount": round(random.uniform(100, 10000), 2),  # Efficient random float range
            "policy_start_date": policy_start_date.strftime("%Y-%m-%d"),
            "policy_end_date": policy_end_date.strftime("%Y-%m-%d"),
            "claim_status": random.choice(["Approved", "Pending", "Denied", "In Progress"]),
            "claim_amount": round(random.uniform(500, 50000), 2),
            "insurer_name": fake.company(),
            "policy_number": fake.bothify(text="??-#####"),
            "beneficiary_name": fake.name(),
            "contact_number": fake.phone_number(),
            "email": fake.email(),
            "address": fake.address().replace("\n", ", "),  # Format address properly
            "policy_renewal_status": fake.boolean(chance_of_getting_true=70),
            "risk_category": random.choice(["Low", "Medium", "High"]),
            "policy_discount": round(random.uniform(0, 500), 2),
            "underwriter": fake.name(),
            "claim_date": claim_date.strftime("%Y-%m-%d"),
            "policy_status": random.choice(["Active", "Lapsed", "Cancelled"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_insurance_data')
# def download_insurance_data():
#     df = generate_insurance_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="insurance_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_insurance_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
