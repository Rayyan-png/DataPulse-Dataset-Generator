from faker import Faker
import pandas as pd
import random
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_educational_data(num_records=100):
    data = [{
        "student_id": fake.uuid4(),
        "student_name": fake.name(),
        "age": random.randint(18, 30),
        "gender": fake.random_element(elements=["Male", "Female", "Non-Binary"]),
        "course_name": fake.random_element(elements=["Computer Science", "Mathematics", "Physics", "Biology", "Economics", "History", "Literature", "Engineering"]),
        "enrollment_year": random.randint(2015, 2024),
        "gpa": round(random.uniform(2.0, 4.0), 2),
        "institution_name": fake.company(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address(),
        "course_code": fake.bothify(text="CSE###"),
        "credit_hours": random.randint(1, 4),
        "semester": fake.random_element(elements=["Spring", "Summer", "Fall", "Winter"]),
        "faculty_name": fake.name(),
        "classroom_number": fake.bothify(text="Room ###"),
        "grade": fake.random_element(elements=["A", "B", "C", "D", "F"]),
        "scholarship_status": fake.random_element(elements=["Yes", "No"]),
        "graduation_status": fake.random_element(elements=["Graduated", "In Progress", "Dropped Out"]),
        "student_club": fake.random_element(elements=["Robotics Club", "Drama Society", "Sports Club", "Music Club", "Debate Club"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_educational_data')
# def download_educational_data():
#     df = generate_educational_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
    
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='educational_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_educational_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
