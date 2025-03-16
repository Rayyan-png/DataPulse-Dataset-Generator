from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_plant_id():
    return fake.uuid4()

def generate_energy_type():
    return fake.random_element(elements=["Solar", "Wind", "Hydro", "Geothermal", "Biomass"])

def generate_capacity_mw():
    return round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2)

def generate_location():
    return fake.city()

def generate_operator():
    return fake.company()

def generate_commission_date():
    return fake.date_this_century()

def generate_energy_output_mwh():
    return round(fake.pyfloat(left_digits=5, right_digits=2, positive=True), 2)

def generate_carbon_offset_tons():
    return round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2)

def generate_grid_connection_status():
    return fake.random_element(elements=["Connected", "Pending", "Disconnected"])

def generate_funding_source():
    return fake.random_element(elements=["Government", "Private", "Public-Private Partnership"])

def generate_project_cost():
    return round(fake.pydecimal(left_digits=7, right_digits=2, positive=True), 2)

def generate_maintenance_frequency():
    return fake.random_element(elements=["Monthly", "Quarterly", "Annually"])

def generate_energy_storage_capacity_mwh():
    return round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2)

def generate_regulatory_compliance():
    return fake.random_element(elements=["Compliant", "Non-Compliant", "Pending Approval"])

def generate_employment_count():
    return fake.random_int(min=5, max=500)

def generate_power_purchase_agreement():
    return fake.random_element(elements=["Active", "Expired", "In Negotiation"])

def generate_technology_type():
    return fake.random_element(elements=["Photovoltaic", "Concentrated Solar Power", "Onshore Wind", "Offshore Wind", "Run-of-River Hydro"])

def generate_environmental_impact_score():
    return round(fake.pyfloat(left_digits=2, right_digits=1, positive=True), 1)

def generate_renewable_energy_data(num_records=100):
    data = [{
        "plant_id": generate_plant_id(),
        "energy_type": generate_energy_type(),
        "capacity_mw": generate_capacity_mw(),
        "location": generate_location(),
        "operator": generate_operator(),
        "commission_date": generate_commission_date(),
        "energy_output_mwh": generate_energy_output_mwh(),
        "carbon_offset_tons": generate_carbon_offset_tons(),
        "grid_connection_status": generate_grid_connection_status(),
        "funding_source": generate_funding_source(),
        "project_cost": generate_project_cost(),
        "maintenance_frequency": generate_maintenance_frequency(),
        "energy_storage_capacity_mwh": generate_energy_storage_capacity_mwh(),
        "regulatory_compliance": generate_regulatory_compliance(),
        "employment_count": generate_employment_count(),
        "power_purchase_agreement": generate_power_purchase_agreement(),
        "technology_type": generate_technology_type(),
        "environmental_impact_score": generate_environmental_impact_score()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_renewable_energy_data')
# def download_renewable_energy_data():
#     df = generate_renewable_energy_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='renewable_energy_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_renewable_energy_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)