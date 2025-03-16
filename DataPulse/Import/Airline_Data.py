from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_flight_number():
    return fake.bothify("??###")

def generate_airline_name():
    return fake.company()

def generate_departure_city():
    return fake.city()

def generate_arrival_city():
    return fake.city()

def generate_departure_time():
    return fake.date_time_between(start_date="-1y", end_date="now")

def generate_arrival_time():
    return fake.date_time_between(start_date="now", end_date="+1y")

def generate_flight_duration():
    return fake.random_int(min=1, max=15)

def generate_ticket_price():
    return round(fake.pydecimal(left_digits=4, right_digits=2, positive=True), 2)

def generate_seat_class():
    return fake.random_element(elements=["Economy", "Business", "First Class"])

def generate_passenger_count():
    return fake.random_int(min=50, max=300)

def generate_gate_number():
    return fake.bothify("G##")

def generate_terminal():
    return fake.bothify("T#")

def generate_aircraft_type():
    return fake.random_element(elements=["Boeing 747", "Airbus A320", "Embraer 190", "Boeing 777"])

def generate_flight_status():
    return fake.random_element(elements=["On Time", "Delayed", "Cancelled"])

def generate_pilot_name():
    return fake.name()

def generate_co_pilot_name():
    return fake.name()

def generate_flight_data(num_records=100):
    data = [{
        "flight_number": generate_flight_number(),
        "airline_name": generate_airline_name(),
        "departure_city": generate_departure_city(),
        "arrival_city": generate_arrival_city(),
        "departure_time": generate_departure_time(),
        "arrival_time": generate_arrival_time(),
        "flight_duration": generate_flight_duration(),
        "ticket_price": generate_ticket_price(),
        "seat_class": generate_seat_class(),
        "passenger_count": generate_passenger_count(),
        "gate_number": generate_gate_number(),
        "terminal": generate_terminal(),
        "aircraft_type": generate_aircraft_type(),
        "flight_status": generate_flight_status(),
        "pilot_name": generate_pilot_name(),
        "co_pilot_name": generate_co_pilot_name()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_airline_data')
# def download_airline_data():
#     df = generate_flight_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='airline_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_flight_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
