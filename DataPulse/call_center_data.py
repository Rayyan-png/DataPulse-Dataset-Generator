from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate call center data
def generate_data(num_records=100):
    data = [{
        "call_id": str(fake.uuid4()),
        "agent_id": fake.random_int(min=100000, max=999999),
        "customer_id": str(fake.uuid4()),
        "call_duration": random.randint(1, 60),  # Call duration in minutes
        "call_type": random.choice(["Inbound", "Outbound"]),
        "call_status": random.choice(["Completed", "Missed", "Dropped"]),
        "call_timestamp": fake.date_time_this_year(),
        "customer_satisfaction": random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]),
        "issue_category": random.choice(["Billing", "Technical Support", "General Inquiry", "Complaint"]),
        "resolution_status": random.choice(["Resolved", "Pending", "Escalated"]),
        "call_rating": random.randint(1, 5),
        "agent_name": fake.name(),
        "call_center_location": fake.city(),
        "follow_up_required": random.choice([True, False]),
        "escalation_level": random.choice(["None", "Level 1", "Level 2", "Level 3"]),
        "feedback_comments": fake.sentence(),
        "hold_duration": random.randint(0, 15),  # Hold time in minutes
        "call_language": random.choice(["English", "Spanish", "French", "German", "Chinese"]),
        "call_channel": random.choice(["Phone", "Chat", "Email"]),
        "priority_level": random.choice(["Low", "Medium", "High"])
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download generated data as CSV
# @app.route('/download_call_center_data')
# def download_call_center_data():
#     df = generate_call_center_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="call_center_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
