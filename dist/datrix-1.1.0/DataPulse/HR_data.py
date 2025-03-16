from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate HR data
def generate_hr_data(num_records=100):
    data = []
    for _ in range(num_records):
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)

        data.append({
            "employee_id": str(fake.uuid4()),  # Ensure UUID is a string
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "department": random.choice(["HR", "IT", "Finance", "Marketing", "Sales", "Operations"]),
            "position": fake.job(),
            "hire_date": hire_date.strftime("%Y-%m-%d"),
            "salary": round(fake.pyfloat(left_digits=5, right_digits=2, positive=True, min_value=30000, max_value=150000), 2),
            "email": fake.company_email(),
            "phone_number": fake.phone_number(),
            "performance_rating": random.choice(["Excellent", "Good", "Average", "Below Average", "Poor"]),
            "employment_status": random.choice(["Active", "On Leave", "Terminated"]),
            "manager_id": str(fake.uuid4()),  # Ensure UUID is a string
            "birth_date": birth_date.strftime("%Y-%m-%d"),
            "gender": random.choice(["Male", "Female", "Other"]),
            "address": fake.address(),
            "work_location": fake.city(),
            "contract_type": random.choice(["Full-Time", "Part-Time", "Contract", "Internship"]),
            "benefit_plan": random.choice(["Basic", "Standard", "Premium", "Executive"]),
            "leave_balance": random.randint(0, 30),
            "promotion_status": random.choice([True, False]),
        })

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_hr_data')
# def download_hr_data():
#     df = generate_hr_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="hr_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_hr_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
