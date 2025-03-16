from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_exporter_name():
    return fake.company()

def generate_importer_name():
    return fake.company()

def generate_product_name():
    return fake.word().capitalize()

def generate_product_category():
    return fake.random_element(elements=["Electronics", "Automobile", "Textiles", "Pharmaceuticals", "Agriculture"])

def generate_export_country():
    return fake.country()

def generate_import_country():
    return fake.country()

def generate_shipment_date():
    return fake.date_between(start_date="-2y", end_date="today")

def generate_arrival_date():
    return fake.date_between(start_date="today", end_date="+1y")

def generate_quantity():
    return fake.random_int(min=10, max=10000)

def generate_unit_price():
    return round(fake.pydecimal(left_digits=5, right_digits=2, positive=True), 2)

def generate_total_value():
    return round(fake.pydecimal(left_digits=7, right_digits=2, positive=True), 2)

def generate_currency():
    return fake.currency_code()

def generate_transport_mode():
    return fake.random_element(elements=["Air", "Sea", "Road", "Rail"])

def generate_customs_status():
    return fake.random_element(elements=["Cleared", "Pending", "Held for Inspection"])

def generate_tariff_code():
    return fake.bothify("###.##.##")

def generate_shipping_company():
    return fake.company()

def generate_port_of_origin():
    return fake.city()

def generate_port_of_destination():
    return fake.city()

def generate_tracking_id():
    return fake.uuid4()

def generate_inspection_status():
    return fake.random_element(elements=["Passed", "Failed", "Not Required"])

def generate_import_export_data(num_records=100):
    data = [{
        "exporter_name": generate_exporter_name(),
        "importer_name": generate_importer_name(),
        "product_name": generate_product_name(),
        "product_category": generate_product_category(),
        "export_country": generate_export_country(),
        "import_country": generate_import_country(),
        "shipment_date": generate_shipment_date(),
        "arrival_date": generate_arrival_date(),
        "quantity": generate_quantity(),
        "unit_price": generate_unit_price(),
        "total_value": generate_total_value(),
        "currency": generate_currency(),
        "transport_mode": generate_transport_mode(),
        "customs_status": generate_customs_status(),
        "tariff_code": generate_tariff_code(),
        "shipping_company": generate_shipping_company(),
        "port_of_origin": generate_port_of_origin(),
        "port_of_destination": generate_port_of_destination(),
        "tracking_id": generate_tracking_id(),
        "inspection_status": generate_inspection_status()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_import_export_data')
# def download_import_export_data():
#     df = generate_import_export_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='import_export_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_import_export_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
