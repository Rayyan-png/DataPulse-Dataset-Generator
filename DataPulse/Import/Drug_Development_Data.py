from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_drug_id():
    return fake.uuid4()

def generate_drug_name():
    return fake.company() + "-" + fake.bothify(text="??-###")

def generate_chemical_composition():
    return ", ".join(fake.words(nb=5))

def generate_clinical_phase():
    return fake.random_element(elements=["Phase 1", "Phase 2", "Phase 3", "Preclinical"])

def generate_approval_status():
    return fake.random_element(elements=["Pending", "Approved", "Rejected", "In Review"])

def generate_manufacturer():
    return fake.company()

def generate_dosage_form():
    return fake.random_element(elements=["Tablet", "Capsule", "Injection", "Syrup"])

def generate_target_disease():
    return fake.random_element(elements=["Cancer", "Diabetes", "Hypertension", "Alzheimer's", "COVID-19"])

def generate_trial_location():
    return fake.city()

def generate_patient_count():
    return fake.random_int(min=50, max=5000)

def generate_side_effects():
    return ", ".join(fake.words(nb=3))

def generate_trial_start_date():
    return fake.date_this_decade()

def generate_trial_end_date():
    return fake.date_this_decade()

def generate_principal_investigator():
    return fake.name()

def generate_drug_cost():
    return round(fake.pydecimal(left_digits=4, right_digits=2, positive=True), 2)

def generate_storage_conditions():
    return fake.random_element(elements=["Room Temperature", "Refrigerated", "Frozen"])

def generate_batch_number():
    return fake.bothify(text="BATCH-#####")

def generate_patent_status():
    return fake.random_element(elements=["Filed", "Granted", "Expired"])

def generate_competing_drugs():
    return ", ".join([fake.company() for _ in range(2)])

def generate_drug_development_data(num_records=100):
    data = [{
        "drug_id": generate_drug_id(),
        "drug_name": generate_drug_name(),
        "chemical_composition": generate_chemical_composition(),
        "clinical_phase": generate_clinical_phase(),
        "approval_status": generate_approval_status(),
        "manufacturer": generate_manufacturer(),
        "dosage_form": generate_dosage_form(),
        "target_disease": generate_target_disease(),
        "trial_location": generate_trial_location(),
        "patient_count": generate_patient_count(),
        "side_effects": generate_side_effects(),
        "trial_start_date": generate_trial_start_date(),
        "trial_end_date": generate_trial_end_date(),
        "principal_investigator": generate_principal_investigator(),
        "drug_cost": generate_drug_cost(),
        "storage_conditions": generate_storage_conditions(),
        "batch_number": generate_batch_number(),
        "patent_status": generate_patent_status(),
        "competing_drugs": generate_competing_drugs()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_drug_development_data')
# def download_drug_development_data():
#     df = generate_drug_development_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='drug_development_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_drug_development_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)