from faker import Faker
import pandas as pd

fake = Faker()

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "employee_id": fake.uuid4(),
            "name": fake.name(),
            "age": fake.random_int(min=22, max=65),
            "gender": fake.random_element(elements=["Male", "Female", "Non-Binary"]),
            "department": fake.random_element(elements=["HR", "Finance", "IT", "Marketing", "Sales", "Operations"]),
            "position": fake.job(),
            "salary": fake.random_int(min=30000, max=150000),
            "hire_date": fake.date_this_decade(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "employment_status": fake.random_element(elements=["Active", "On Leave", "Resigned", "Terminated"])
        })
    
    return pd.DataFrame(data)

# Generate sample data and save to CSV
df = generate_data(500)
df.to_csv("employee_data.csv", index=False)
print("Employee data generated and saved to employee_data.csv")
