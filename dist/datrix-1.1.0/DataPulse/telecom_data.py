from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate telecommunication data
def generate_telecommunication_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "subscriber_id": str(fake.uuid4()),
            "phone_number": fake.phone_number(),
            "plan_type": random.choice(["Prepaid", "Postpaid", "Family", "Business"]),
            "data_usage_gb": round(random.uniform(0, 100), 2),  # Adjusted realistic data usage
            "call_duration_min": round(random.uniform(0, 1000), 1),  # Adjusted realistic call duration
            "sms_count": random.randint(0, 500),
            "billing_amount": round(random.uniform(0, 500), 2),  # Adjusted realistic billing amount
            "service_provider": fake.company(),
            "country": fake.country(),
            "city": fake.city(),
            "connection_type": random.choice(["4G", "5G", "Fiber", "DSL"]),
            "activation_date": fake.date_this_decade().strftime("%Y-%m-%d"),
            "payment_status": random.choice(["Paid", "Pending", "Overdue"]),
            "customer_age": random.randint(18, 85),
            "device_type": random.choice(["Smartphone", "Tablet", "Router", "Smartwatch"]),
            "network_latency_ms": random.randint(10, 500),
            "contract_duration_months": random.randint(1, 36),
            "ip_address": fake.ipv4(),
            "customer_satisfaction": random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]),
            "data_roaming": random.choices([True, False], weights=[20, 80])[0]  # 20% chance of roaming
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_telecommunication_data')
# def download_telecommunication_data():
#     df = generate_telecommunication_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="telecommunication_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_telecommunication_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
