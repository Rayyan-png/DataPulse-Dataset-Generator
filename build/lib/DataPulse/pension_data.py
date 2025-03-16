from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate pension data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "pensioner_name": fake.name(),
            "pension_type": random.choice(["Government Pension", "Private Pension", "Social Security", "Retirement Savings Plan"]),
            "pension_amount": round(random.uniform(10000, 500000), 2),
            "currency": fake.currency_code(),
            "retirement_date": fake.date_between(start_date="-30y", end_date="today").strftime("%Y-%m-%d"),
            "pension_status": random.choice(["Active", "Inactive", "Suspended", "Terminated"]),
            "contribution_amount": round(random.uniform(5000, 100000), 2),
            "beneficiary_name": fake.name(),
            "benefit_frequency": random.choice(["Monthly", "Quarterly", "Annually"]),
            "plan_id": fake.bothify("PLAN-####"),
            "insurer_name": fake.company(),
            "payout_amount": round(random.uniform(10000, 500000), 2),
            "tax_rate": round(random.uniform(0.01, 0.5), 2),
            "pension_id": str(fake.uuid4()),
            "advisor_name": fake.name(),
            "geographical_region": fake.country(),
            "employer_contribution": round(random.uniform(5000, 100000), 2),
            "retirement_age": random.randint(55, 70),
            "withdrawal_date": fake.date_between(start_date="today", end_date="+20y").strftime("%Y-%m-%d"),
            "investment_strategy": random.choice(["Conservative", "Balanced", "Growth", "Aggressive"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_pension_data')
# def download_pension_data():
#     df = generate_pension_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="pension_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_pension_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
