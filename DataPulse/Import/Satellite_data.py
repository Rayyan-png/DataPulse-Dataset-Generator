from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_satellite_id():
    return fake.uuid4()

def generate_launch_date():
    return fake.date_this_century()

def generate_orbit_type():
    return fake.random_element(elements=["Low Earth Orbit", "Medium Earth Orbit", "Geostationary Orbit", "Polar Orbit"])

def generate_operator():
    return fake.company()

def generate_mission_type():
    return fake.random_element(elements=["Communication", "Earth Observation", "Navigation", "Scientific Research", "Military"])

def generate_country():
    return fake.country()

def generate_status():
    return fake.random_element(elements=["Active", "Inactive", "Decommissioned", "In Development"])

def generate_signal_frequency():
    return f"{fake.random_int(min=1000, max=30000)} MHz"

def generate_weight():
    return fake.random_int(min=100, max=10000)

def generate_power_capacity():
    return f"{fake.random_int(min=500, max=20000)} W"

def generate_lifespan():
    return fake.random_int(min=1, max=30)

def generate_launch_site():
    return fake.city()

def generate_satellite_data(num_records=100):
    data = [{
        "satellite_id": generate_satellite_id(),
        "launch_date": generate_launch_date(),
        "orbit_type": generate_orbit_type(),
        "operator": generate_operator(),
        "mission_type": generate_mission_type(),
        "country": generate_country(),
        "status": generate_status(),
        "signal_frequency": generate_signal_frequency(),
        "weight_kg": generate_weight(),
        "power_capacity_watts": generate_power_capacity(),
        "lifespan_years": generate_lifespan(),
        "launch_site": generate_launch_site()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_satellite_data')
# def download_satellite_data():
#     df = generate_satellite_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='satellite_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_satellite_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
