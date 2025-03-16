from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate copyright dataset
def generate_data(num_records=100):
    data = [{
        "copyright_id": str(fake.uuid4()),
        "title": fake.catch_phrase(),
        "owner_name": fake.name(),
        "registration_date": fake.date_this_decade(),
        "expiration_date": fake.date_between(start_date="+10y", end_date="+20y"),
        "work_type": random.choice(["Literary", "Musical", "Artistic", "Software", "Broadcast"]),
        "jurisdiction": fake.country(),
        "infringement_cases": random.randint(0, 20),
        "license_type": random.choice(["Exclusive", "Non-exclusive", "Public Domain"]),
        "license_fee": round(random.uniform(1000.00, 50000.00), 2),  # License fee in currency
        "ip_status": random.choice(["Active", "Expired", "Pending", "Disputed"]),
        "renewal_flag": random.choice([True, False]),
        "application_number": fake.bothify("APP###-#####"),
        "grant_number": fake.bothify("GRN###-#####"),
        "publication_date": fake.date_this_decade(),
        "court_decision": random.choice(["Upheld", "Overturned", "Settled", "Pending"]),
        "agent_name": fake.name(),
        "agency_name": fake.company(),
        "related_works": random.randint(0, 10),
        "commercial_use": random.choice([True, False])
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_copyright_data')
# def download_copyright_data():
#     df = generate_copyright_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="copyright_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
