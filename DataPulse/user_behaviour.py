from faker import Faker
import pandas as pd
from flask import Flask, send_file

fake = Faker()

app = Flask(__name__)

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "user_id": fake.uuid4(),
            "session_id": fake.uuid4(),
            "page_views": fake.random_int(min=1, max=50),
            "clicks": fake.random_int(min=0, max=100),
            "time_spent_seconds": fake.random_int(min=10, max=5000),
            "bounce_rate": round(fake.random_number(digits=2) / 100, 2),
            "device_type": fake.random_element(elements=["Mobile", "Desktop", "Tablet"]),
            "browser": fake.random_element(elements=["Chrome", "Firefox", "Safari", "Edge", "Opera"]),
            "location": fake.city(),
            "session_start": fake.date_time_this_year(),
            "session_end": fake.date_time_this_year(),
            "conversion": fake.random_element(elements=["Yes", "No"]),
        })
    
    return pd.DataFrame(data)

# @app.route('/download_user_behavior_data')
# def download_user_behavior_data():
#     df = generate_user_behavior_data(5000)
#     file_path = "user_behavior_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
