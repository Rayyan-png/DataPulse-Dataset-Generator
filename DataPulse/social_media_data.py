from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate social media data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "user_id": str(fake.uuid4()),
            "username": fake.user_name(),
            "email": fake.email(),
            "platform": random.choice(["Facebook", "Twitter", "Instagram", "LinkedIn", "TikTok", "Snapchat"]),
            "post_id": str(fake.uuid4()),
            "post_content": fake.sentence(nb_words=20),
            "post_date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "like_count": random.randint(0, 10000),
            "comment_count": random.randint(0, 5000),
            "share_count": random.randint(0, 3000),
            "followers_count": random.randint(0, 1000000),
            "following_count": random.randint(0, 5000),
            "profile_creation_date": fake.date_this_decade().strftime("%Y-%m-%d"),
            "account_status": random.choice(["Active", "Inactive", "Suspended"]),
            "hashtags": ", ".join(fake.words(nb=5)),
            "location": fake.city(),
            "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
            "engagement_rate": round(random.uniform(0, 1), 4),
            "content_type": random.choice(["Text", "Image", "Video", "Link"]),
            "ad_impressions": random.randint(0, 100000),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_social_media_data')
# def download_social_media_data():
#     df = generate_social_media_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="social_media_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_social_media_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
