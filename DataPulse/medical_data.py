from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate medical data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        admission_date = fake.date_this_decade()
        discharge_date = fake.date_between(start_date=admission_date, end_date='today')  # Ensuring discharge date is after admission
        followup_date = fake.date_between(start_date='today', end_date='+6m')

        data.append({
            "patient_id": str(fake.uuid4()),
            "patient_name": fake.name(),
            "age": random.randint(0, 100),
            "gender": random.choice(["Male", "Female", "Other"]),
            "diagnosis": random.choice(["Hypertension", "Diabetes", "Asthma", "Flu", "Migraine"]),
            "admission_date": admission_date.strftime("%Y-%m-%d"),
            "discharge_date": discharge_date.strftime("%Y-%m-%d"),
            "doctor_name": fake.name(),
            "department": random.choice(["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General Medicine"]),
            "medication": random.choice(["Aspirin", "Metformin", "Lisinopril", "Ibuprofen", "Amoxicillin"]),
            "allergies": random.choice(["None", "Penicillin", "Peanuts", "Shellfish", "Latex"]),
            "blood_type": random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),
            "insurance_provider": fake.company(),
            "policy_number": fake.bothify("??###-###-####"),
            "emergency_contact": fake.phone_number(),
            "visit_type": random.choice(["Inpatient", "Outpatient", "Emergency"]),
            "procedure": random.choice(["MRI", "CT Scan", "X-Ray", "Blood Test", "Surgery"]),
            "hospital_name": fake.company(),
            "billing_amount": round(random.uniform(100.00, 50000.00), 2),  # Ensuring realistic billing amounts
            "followup_date": followup_date.strftime("%Y-%m-%d"),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_medical_data')
# def download_medical_data():
#     df = generate_medical_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="medical_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_medical_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
