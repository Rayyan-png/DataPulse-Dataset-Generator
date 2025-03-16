from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate demographic dataset
def generate_data(num_records=100):
    data = [{
        "person_id": str(fake.uuid4()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female", "Non-Binary", "Other"]),
        "age": random.randint(1, 100),
        "birth_date": fake.date_of_birth(minimum_age=1, maximum_age=100).strftime("%Y-%m-%d"),
        "ethnicity": random.choice(["Asian", "Black", "Hispanic", "White", "Mixed", "Other"]),
        "nationality": fake.country(),
        "language": fake.language_name(),
        "education_level": random.choice(["Primary", "Secondary", "High School", "Bachelor's", "Master's", "Doctorate"]),
        "occupation": fake.job(),
        "income_level": random.choice(["Low", "Middle", "High"]),
        "marital_status": random.choice(["Single", "Married", "Divorced", "Widowed"]),
        "household_size": random.randint(1, 10),
        "religion": random.choice(["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "None", "Other"]),
        "residence_type": random.choice(["Urban", "Suburban", "Rural"]),
        "employment_status": random.choice(["Employed", "Unemployed", "Retired", "Student"]),
        "health_status": random.choice(["Excellent", "Good", "Fair", "Poor"]),
        "political_affiliation": random.choice(["Liberal", "Conservative", "Independent", "Other"]),
        "citizenship_status": random.choice(["Citizen", "Permanent Resident", "Temporary Resident", "Undocumented"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_demographic_data')
# def download_demographic_data():
#     df = generate_demographic_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="demographic_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
