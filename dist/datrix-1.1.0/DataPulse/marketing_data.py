from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate marketing data
def generate_marketing_data(num_records=100):
    data = []
    for _ in range(num_records):
        start_date = fake.date_between(start_date='-2y', end_date='-1y')
        end_date = fake.date_between(start_date=start_date, end_date='today')  # Ensuring end_date is after start_date

        data.append({
            "campaign_id": str(fake.uuid4()),
            "campaign_name": fake.catch_phrase(),
            "channel": random.choice(["Email", "Social Media", "TV", "Radio", "Online Ads", "Print Media"]),
            "budget": round(random.uniform(1000.00, 10000000.00), 2),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "target_audience": random.choice(["Teenagers", "Adults", "Seniors", "Businesses", "Students"]),
            "conversion_rate": round(random.uniform(0.01, 0.5), 4),
            "impressions": random.randint(1000, 1000000),
            "clicks": random.randint(100, 100000),
            "cost_per_click": round(random.uniform(0.01, 100.00), 2),
            "roi": round(random.uniform(0.01, 20.00), 2),
            "region": random.choice(["North America", "Europe", "Asia", "South America", "Africa", "Oceania"]),
            "ad_type": random.choice(["Banner", "Video", "Pop-up", "Native"]),
            "campaign_status": random.choice(["Active", "Completed", "Paused", "Cancelled"]),
            "lead_count": random.randint(10, 10000),
            "customer_acquisition_cost": round(random.uniform(100.00, 10000.00), 2),
            "engagement_rate": round(random.uniform(0.01, 0.3), 4),
            "revenue": round(random.uniform(1000.00, 10000000.00), 2),
            "feedback": fake.sentence(nb_words=10),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_marketing_data')
# def download_marketing_data():
#     df = generate_marketing_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="marketing_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_marketing_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
