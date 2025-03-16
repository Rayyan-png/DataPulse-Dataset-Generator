from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate government service data
def generate_government_data(num_records=100):
    data = []
    for _ in range(num_records):
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
        request_date = fake.date_this_year()

        data.append({
            "citizen_id": str(fake.uuid4()),  # Ensure UUID is a string
            "full_name": fake.name(),
            "birth_date": birth_date.strftime("%Y-%m-%d"),  # Format date
            "address": fake.address(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country(),
            "postal_code": fake.postcode(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "department": random.choice(["Health", "Education", "Transportation", "Public Safety", "Housing", "Environment"]),
            "service_type": random.choice(["Social Welfare", "Public Works", "Policy Implementation", "Emergency Response", "Community Outreach"]),
            "application_id": fake.bothify(text="APP-###-????"),
            "request_date": request_date.strftime("%Y-%m-%d"),  # Format date
            "processing_status": random.choice(["Pending", "In Progress", "Completed", "Rejected"]),
            "service_fee": round(fake.pydecimal(left_digits=3, right_digits=2, positive=True), 2),
            "case_officer": fake.name(),
            "service_location": fake.city(),
            "beneficiary_type": random.choice(["Individual", "Organization", "Community Group"]),
            "policy_reference": fake.bothify(text="POL-####-????"),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_government_data')
# def download_government_data():
#     df = generate_government_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="government_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_government_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
