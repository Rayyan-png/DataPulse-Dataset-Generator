from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate legal compliance data
def generate_legal_compliance_data(num_records=100):
    data = []
    for _ in range(num_records):
        audit_date = fake.date_this_decade()
        compliance_deadline = fake.date_this_year()

        data.append({
            "compliance_id": str(fake.uuid4()),  # Ensure UUID is a string
            "regulation_name": random.choice(["GDPR", "HIPAA", "CCPA", "SOX", "PCI DSS", "FISMA"]),
            "compliance_status": random.choice(["Compliant", "Non-Compliant", "Pending Review"]),
            "audit_date": audit_date.strftime("%Y-%m-%d"),
            "auditor_name": fake.name(),
            "violation_flag": fake.boolean(chance_of_getting_true=20),
            "fine_amount": round(random.uniform(1000.00, 1000000.00), 2),  # More realistic fines
            "policy_version": fake.bothify("v##.##"),
            "department": random.choice(["Finance", "HR", "IT", "Legal", "Operations"]),
            "remediation_status": random.choice(["Completed", "In Progress", "Not Started"]),
            "risk_level": random.choice(["Low", "Medium", "High", "Critical"]),
            "data_type": random.choice(["Personal Data", "Financial Data", "Medical Data", "Intellectual Property"]),
            "review_cycle": random.choice(["Annual", "Bi-Annual", "Quarterly", "Monthly"]),
            "internal_control": fake.bs(),
            "incident_reported": fake.boolean(chance_of_getting_true=15),
            "third_party_involvement": fake.boolean(chance_of_getting_true=25),
            "compliance_officer": fake.name(),
            "documentation_status": random.choice(["Complete", "Partial", "Missing"]),
            "penalty_type": random.choice(["Monetary", "Operational", "Reputational"]),
            "compliance_deadline": compliance_deadline.strftime("%Y-%m-%d"),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_legal_compliance_data')
# def download_legal_compliance_data():
#     df = generate_legal_compliance_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="legal_compliance_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_legal_compliance_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
