from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_project_id():
    return fake.uuid4()

def generate_project_name():
    return fake.bs().title()

def generate_contractor_name():
    return fake.company()

def generate_project_status():
    return fake.random_element(elements=["Planning", "In Progress", "Completed", "On Hold", "Cancelled"])

def generate_start_date():
    return fake.date_this_decade()

def generate_end_date():
    return fake.date_between(start_date="-1y", end_date="+2y")

def generate_budget():
    return round(fake.pydecimal(left_digits=8, right_digits=2, positive=True), 2)

def generate_location():
    return fake.address()

def generate_project_manager():
    return fake.name()

def generate_materials_cost():
    return round(fake.pydecimal(left_digits=7, right_digits=2, positive=True), 2)

def generate_labor_cost():
    return round(fake.pydecimal(left_digits=7, right_digits=2, positive=True), 2)

def generate_permit_number():
    return fake.bothify(text="??-#####")

def generate_inspection_date():
    return fake.date_between(start_date="-1y", end_date="today")

def generate_subcontractor_name():
    return fake.company()

def generate_project_phase():
    return fake.random_element(elements=["Design", "Foundation", "Framing", "Finishing", "Inspection"])

def generate_equipment_used():
    return fake.random_element(elements=["Excavator", "Crane", "Bulldozer", "Concrete Mixer", "Dump Truck"])

def generate_safety_compliance():
    return fake.boolean(chance_of_getting_true=90)

def generate_daily_workforce():
    return fake.random_int(min=10, max=500)

def generate_environmental_impact():
    return fake.random_element(elements=["Low", "Moderate", "High"])

def generate_construction_data(num_records=100):
    data = [{
        "project_id": generate_project_id(),
        "project_name": generate_project_name(),
        "contractor_name": generate_contractor_name(),
        "project_status": generate_project_status(),
        "start_date": generate_start_date(),
        "end_date": generate_end_date(),
        "budget": generate_budget(),
        "location": generate_location(),
        "project_manager": generate_project_manager(),
        "materials_cost": generate_materials_cost(),
        "labor_cost": generate_labor_cost(),
        "permit_number": generate_permit_number(),
        "inspection_date": generate_inspection_date(),
        "subcontractor_name": generate_subcontractor_name(),
        "project_phase": generate_project_phase(),
        "equipment_used": generate_equipment_used(),
        "safety_compliance": generate_safety_compliance(),
        "daily_workforce": generate_daily_workforce(),
        "environmental_impact": generate_environmental_impact()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_construction_data')
# def download_construction_data():
#     df = generate_construction_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='construction_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_construction_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)