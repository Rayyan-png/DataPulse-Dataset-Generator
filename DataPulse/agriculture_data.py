from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io
import random

fake = Faker()
app = Flask(__name__)

def generate_farm_id():
    return str(fake.uuid4())  # Ensure UUID is a string

def generate_crop_type():
    return random.choice(["Wheat", "Corn", "Rice", "Soybean", "Barley", "Cotton"])

def generate_yield_quantity_kg():
    return round(random.uniform(100.0, 5000.0), 2)  # No pyfloat issues

def generate_harvest_date():
    return fake.date_this_year()

def generate_soil_type():
    return random.choice(["Sandy", "Clay", "Silt", "Loam", "Peat"])

def generate_irrigation_method():
    return random.choice(["Drip", "Flood", "Sprinkler", "Manual"])

def generate_fertilizer_used():
    return random.choice(["Nitrogen", "Phosphorus", "Potassium", "Organic", "None"])

def generate_weather_condition():
    return random.choice(["Sunny", "Rainy", "Cloudy", "Stormy", "Windy"])

def generate_field_size_hectares():
    return round(random.uniform(1.0, 100.0), 2)  # No pyfloat issues

def generate_pesticide_applied():
    return random.choice([True, False])

def generate_farmer_name():
    return fake.name()

def generate_farm_location():
    return fake.city()

def generate_seed_variety():
    return fake.word()

def generate_crop_health():
    return random.choice(["Healthy", "Diseased", "Pest-Infested", "Drought-Affected"])

def generate_market_price_per_kg():
    return round(random.uniform(1.0, 50.0), 2)  # No pyfloat issues

def generate_organic_certified():
    return random.choice([True, False])

def generate_machinery_used():
    return random.choice(["Tractor", "Combine Harvester", "Plow", "Seeder", "Manual"])

def generate_water_source():
    return random.choice(["Well", "River", "Rainwater", "Irrigation Canal"])

def generate_planting_date():
    return fake.date_this_year()

def generate_crop_rotation():
    return random.choice([True, False])

def generate_data(num_records=100):
    data = [{
        "farm_id": generate_farm_id(),
        "crop_type": generate_crop_type(),
        "yield_quantity_kg": generate_yield_quantity_kg(),
        "harvest_date": generate_harvest_date(),
        "soil_type": generate_soil_type(),
        "irrigation_method": generate_irrigation_method(),
        "fertilizer_used": generate_fertilizer_used(),
        "weather_condition": generate_weather_condition(),
        "field_size_hectares": generate_field_size_hectares(),
        "pesticide_applied": generate_pesticide_applied(),
        "farmer_name": generate_farmer_name(),
        "farm_location": generate_farm_location(),
        "seed_variety": generate_seed_variety(),
        "crop_health": generate_crop_health(),
        "market_price_per_kg": generate_market_price_per_kg(),
        "organic_certified": generate_organic_certified(),
        "machinery_used": generate_machinery_used(),
        "water_source": generate_water_source(),
        "planting_date": generate_planting_date(),
        "crop_rotation": generate_crop_rotation()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

@app.route('/download_agricultural_data')
def download_agricultural_data():
    df = generate_data(num_records=500000)
    output = io.BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='agricultural_data.csv')

if __name__ == '__main__':
    sample_df = generate_data(10)
    print(sample_df.head(10))
    app.run(debug=True)
