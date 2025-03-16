from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate survey data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "survey_id": str(fake.uuid4()),
            "respondent_id": str(fake.uuid4()),
            "survey_title": fake.sentence(nb_words=5),
            "question": fake.sentence(nb_words=10),
            "response": random.choice(["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
            "response_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "location": fake.city(),
            "age": random.randint(18, 80),
            "gender": random.choice(["Male", "Female", "Non-Binary", "Prefer Not to Say"]),
            "income_level": random.choice(["Low", "Medium", "High"]),
            "education_level": random.choice(["High School", "Bachelor's", "Master's", "PhD"]),
            "satisfaction_score": random.randint(1, 10),
            "feedback": fake.paragraph(nb_sentences=2),
            "device_used": random.choice(["Mobile", "Desktop", "Tablet"]),
            "channel": random.choice(["Email", "Website", "In-person", "Phone"]),
            "follow_up_required": random.choices([True, False], weights=[20, 80])[0],  # 20% chance of follow-up
            "time_spent": random.randint(1, 60),  # Time in minutes
            "ip_address": fake.ipv4(),
            "language": random.choice(["English", "Spanish", "French", "German", "Chinese"]),
            "survey_type": random.choice(["Customer Satisfaction", "Market Research", "Employee Feedback", "Product Review"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_survey_data')
# def download_survey_data():
#     df = generate_survey_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="survey_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_survey_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
