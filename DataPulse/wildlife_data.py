from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Wildlife Conservation dataset
def generate_data(num_records=100):
    data = [{
        "species_id": fake.bothify("SP-####"),
        "species_name": random.choice(["Tiger", "Elephant", "Panda", "Lion", "Rhino", "Gorilla", "Leopard", "Sea Turtle", "Snow Leopard", "Orangutan"]),
        "habitat": random.choice(["Forest", "Grassland", "Wetland", "Desert", "Mountain", "Marine", "Savannah"]),
        "conservation_status": random.choice(["Endangered", "Critically Endangered", "Vulnerable", "Near Threatened", "Least Concern"]),
        "population_estimate": random.randint(10, 10000),
        "protected_area": random.choice(["National Park", "Wildlife Sanctuary", "Biosphere Reserve", "Marine Reserve", "Game Reserve"]),
        "location": f"{fake.city()}, {fake.country()}",
        "tracking_id": str(fake.uuid4()),
        "last_sighting": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
        "researcher_name": fake.name(),
        "project_name": fake.catch_phrase(),
        "funding_source": fake.company(),
        "monitoring_method": random.choice(["Camera Trap", "GPS Collar", "Direct Observation", "Acoustic Monitoring", "Satellite Imaging"]),
        "health_status": random.choice(["Healthy", "Injured", "Deceased", "Unknown"]),
        "species_behavior": random.choice(["Migrating", "Foraging", "Resting", "Breeding", "Hunting"]),
        "climate_condition": random.choice(["Sunny", "Rainy", "Snowy", "Cloudy", "Stormy"]),
        "conservation_agency": fake.company(),
        "protection_level": random.choice(["High", "Medium", "Low"]),
        "field_station": fake.bothify("FS-##-??"),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_wildlife_conservation_data')
# def download_wildlife_conservation_data():
#     df = generate_wildlife_conservation_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="wildlife_conservation_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_wildlife_conservation_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
