from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_station_id():
    return fake.uuid4()

def generate_station_name():
    return fake.city() + " Climate Station"

def generate_temperature():
    return round(fake.pyfloat(min_value=-30, max_value=50, right_digits=1), 1)

def generate_humidity():
    return fake.random_int(min=0, max=100)

def generate_precipitation():
    return round(fake.pyfloat(min_value=0, max_value=500, right_digits=2), 2)

def generate_wind_speed():
    return round(fake.pyfloat(min_value=0, max_value=150, right_digits=2), 2)

def generate_air_pressure():
    return round(fake.pyfloat(min_value=950, max_value=1050, right_digits=2), 2)

def generate_weather_condition():
    return fake.random_element(elements=["Sunny", "Rainy", "Cloudy", "Snowy", "Stormy", "Foggy"])

def generate_measurement_time():
    return fake.date_time_this_year()

def generate_solar_radiation():
    return round(fake.pyfloat(min_value=0, max_value=1200, right_digits=2), 2)

def generate_co2_level():
    return round(fake.pyfloat(min_value=300, max_value=500, right_digits=2), 2)

def generate_climate_data(num_records=100):
    data = [{
        "station_id": generate_station_id(),
        "station_name": generate_station_name(),
        "temperature": generate_temperature(),
        "humidity": generate_humidity(),
        "precipitation": generate_precipitation(),
        "wind_speed": generate_wind_speed(),
        "air_pressure": generate_air_pressure(),
        "weather_condition": generate_weather_condition(),
        "measurement_time": generate_measurement_time(),
        "solar_radiation": generate_solar_radiation(),
        "co2_level": generate_co2_level()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_climate_data')
# def download_climate_data():
#     df = generate_climate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='climate_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_climate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)