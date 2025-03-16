from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate geospatial data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "location_id": str(fake.uuid4()),  # Ensure UUID is a string
            "latitude": round(fake.latitude(), 6),  # Ensure decimal precision
            "longitude": round(fake.longitude(), 6),  # Ensure decimal precision
            "altitude": round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=1, max_value=5000), 2),
            "country": fake.country(),
            "city": fake.city(),
            "zip_code": fake.zipcode(),
            "region": fake.state(),
            "continent": random.choice(["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"]),
            "geohash": fake.bothify(text='?????-#####'),
            "address": fake.address(),
            "landmark": fake.street_name(),
            "population_density": fake.random_int(min=1, max=10000),
            "urban_rural": random.choice(["Urban", "Rural", "Suburban"]),
            "time_zone": fake.timezone(),
            "area_size": round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=1, max_value=10000), 2),
            "climate_zone": random.choice(["Tropical", "Dry", "Temperate", "Continental", "Polar"]),
            "transport_access": random.choice(["Highway", "Railway", "Airport", "Seaport", "None"]),
            "environment_type": random.choice(["Coastal", "Mountainous", "Plains", "Desert", "Forest"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_geospatial_data')
# def download_geospatial_data():
#     df = generate_geospatial_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="geospatial_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_geospatial_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
