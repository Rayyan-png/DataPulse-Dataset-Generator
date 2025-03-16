from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_experiment_id():
    return fake.uuid4()

def generate_experiment_name():
    return fake.sentence(nb_words=4)

def generate_principal_investigator():
    return fake.name()

def generate_institution():
    return fake.company()

def generate_experiment_date():
    return fake.date_this_decade()

def generate_data_type():
    return fake.random_element(elements=["Astronomical Data", "Planetary Data", "Cosmic Radiation", "Satellite Imaging"])

def generate_observation_site():
    return fake.city()

def generate_mission_name():
    return fake.bs()

def generate_sensor_type():
    return fake.random_element(elements=["Infrared", "Ultraviolet", "Radio", "Optical"])

def generate_data_size():
    return f"{fake.random_number(digits=3)} GB"

def generate_analysis_status():
    return fake.random_element(elements=["Pending", "In Progress", "Completed"])

def generate_publication_status():
    return fake.random_element(elements=["Unpublished", "Peer Reviewed", "Preprint"])

def generate_space_science_data(num_records=100):
    data = [{
        "experiment_id": generate_experiment_id(),
        "experiment_name": generate_experiment_name(),
        "principal_investigator": generate_principal_investigator(),
        "institution": generate_institution(),
        "experiment_date": generate_experiment_date(),
        "data_type": generate_data_type(),
        "observation_site": generate_observation_site(),
        "mission_name": generate_mission_name(),
        "sensor_type": generate_sensor_type(),
        "data_size": generate_data_size(),
        "analysis_status": generate_analysis_status(),
        "publication_status": generate_publication_status()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_space_science_data')
# def download_space_science_data():
#     df = generate_space_science_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='space_science_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_space_science_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
