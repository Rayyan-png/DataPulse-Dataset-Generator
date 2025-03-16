from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate urban development data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        start_date = fake.date_between(start_date='-10y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+5y')

        data.append({
            "project_id": str(fake.uuid4()),
            "project_name": fake.company() + " Urban Development",
            "location": fake.city(),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "budget": round(random.uniform(100000, 50000000), 2),  # Budget in USD
            "project_status": random.choice(["Planning", "In Progress", "Completed", "On Hold"]),
            "project_manager": fake.name(),
            "contractor": fake.company(),
            "building_type": random.choice(["Residential", "Commercial", "Industrial", "Mixed-Use"]),
            "zone": random.choice(["Urban", "Suburban", "Rural"]),
            "environmental_impact": random.choice(["Low", "Moderate", "High"]),
            "permits_issued": random.choice([True, False]),
            "population_served": random.randint(500, 100000),
            "green_certification": random.choice(["LEED", "BREEAM", "None"]),
            "public_transport_access": random.choice(["High", "Medium", "Low"]),
            "infrastructure_type": random.choice(["Roads", "Parks", "Utilities", "Mixed"]),
            "funding_source": random.choice(["Government", "Private", "Public-Private Partnership"]),
            "land_area": round(random.uniform(0.5, 10000), 2),  # Area in acres
            "community_involvement": random.choice(["High", "Medium", "Low"])
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_urban_development_data')
# def download_urban_development_data():
#     df = generate_urban_development_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="urban_development_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_urban_development_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
