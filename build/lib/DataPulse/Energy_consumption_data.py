from faker import Faker
import pandas as pd
import random
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_data(num_records=100):
    data = [{
        "meter_id": fake.uuid4(),
        "energy_type": fake.random_element(elements=["Electricity", "Gas", "Solar", "Wind", "Hydro"]),
        "consumption_value": round(random.uniform(100, 9999), 2),
        "unit": fake.random_element(elements=["kWh", "MJ", "Therms", "m³"]),
        "billing_cycle": fake.random_element(elements=["Monthly", "Quarterly", "Annual"]),
        "customer_id": fake.uuid4(),
        "city": fake.city(),
        "country": fake.country(),
        "meter_read_date": fake.date_this_year(),
        "tariff_rate": round(random.uniform(0.01, 9.99), 4),
        "peak_usage": round(random.uniform(10, 999), 2),
        "off_peak_usage": round(random.uniform(10, 999), 2),
        "total_cost": round(random.uniform(50, 9999), 2),
        "provider_name": fake.company(),
        "energy_efficiency_rating": fake.random_element(elements=["A", "B", "C", "D", "E"]),
        "usage_category": fake.random_element(elements=["Residential", "Commercial", "Industrial"]),
        "power_factor": round(random.uniform(0.1, 1.0), 3),
        "carbon_emissions": round(random.uniform(10, 999), 2),
        "invoice_number": fake.bothify(text="INV-#######"),
        "payment_status": fake.random_element(elements=["Paid", "Pending", "Overdue"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_energy_consumption_data')
# def download_energy_consumption_data():
#     df = generate_energy_consumption_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
    
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='energy_consumption_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_energy_consumption_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
