from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate online learning data
def generate_online_learning_data(num_records=100):
    data = []
    for _ in range(num_records):
        enrollment_date = fake.date_this_year()
        completion_date = fake.date_between(start_date=enrollment_date, end_date="today")

        data.append({
            "course_id": str(fake.uuid4()),
            "course_name": fake.sentence(nb_words=4),
            "instructor_name": fake.name(),
            "student_id": str(fake.uuid4()),
            "student_name": fake.name(),
            "enrollment_date": enrollment_date.strftime("%Y-%m-%d"),
            "completion_date": completion_date.strftime("%Y-%m-%d"),
            "course_duration_weeks": random.randint(4, 52),
            "grade": random.choice(["A", "B", "C", "D", "F"]),
            "course_level": random.choice(["Beginner", "Intermediate", "Advanced"]),
            "platform": random.choice(["Udemy", "Coursera", "edX", "Skillshare", "LinkedIn Learning"]),
            "student_age": random.randint(18, 60),
            "country": fake.country(),
            "language": random.choice(["English", "Spanish", "French", "German", "Chinese"]),
            "certification_awarded": random.choice([True, False]),
            "feedback_score": round(random.uniform(0.0, 5.0), 2),
            "device_used": random.choice(["Laptop", "Desktop", "Tablet", "Smartphone"]),
            "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"])
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_online_learning_data')
# def download_online_learning_data():
#     df = generate_online_learning_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="online_learning_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_online_learning_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
