from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate sentiment analysis data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "text_id": str(fake.uuid4()),
            "text": fake.sentence(nb_words=20),
            "sentiment": random.choice(["Positive", "Negative", "Neutral"]),
            "sentiment_score": round(random.uniform(0, 1), 2),
            "language": random.choice(["English", "Spanish", "French", "German", "Chinese"]),
            "source": random.choice(["Social Media", "News", "Product Review", "Customer Feedback", "Survey"]),
            "timestamp": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "author": fake.name(),
            "topic": random.choice(["Politics", "Technology", "Health", "Sports", "Entertainment"]),
            "location": fake.city(),
            "emotion": random.choice(["Happy", "Sad", "Angry", "Excited", "Frustrated"]),
            "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
            "platform": random.choice(["Twitter", "Facebook", "YouTube", "Instagram", "LinkedIn"]),
            "url": fake.url(),
            "keyword": fake.word(),
            "length_of_text": random.randint(50, 500),
            "category": random.choice(["Positive Review", "Complaint", "Inquiry", "General Feedback"]),
            "language_confidence": round(random.uniform(0, 1), 2),
            "user_type": random.choice(["Registered", "Guest", "Anonymous"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_sentiment_data')
# def download_sentiment_data():
#     df = generate_sentiment_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="sentiment_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_sentiment_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
