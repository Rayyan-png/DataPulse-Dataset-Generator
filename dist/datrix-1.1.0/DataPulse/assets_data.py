from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_asset_management_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "asset_id": str(fake.uuid4()),  # Ensure UUID is a string
            "asset_name": random.choice(["Computer", "Vehicle", "Machinery", "Furniture", "Building"]),
            "purchase_date": fake.date_this_decade(),
            "asset_value": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "depreciation_rate": round(random.uniform(0.01, 50.0), 2),  # No pyfloat issues
            "current_value": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "location": fake.city(),
            "asset_status": random.choice(["Active", "In Maintenance", "Retired", "Disposed"]),
            "responsible_person": fake.name(),
            "serial_number": fake.bothify("??-####-??"),
            "warranty_expiration": fake.date_this_decade(),
            "asset_category": random.choice(["Electronics", "Vehicles", "Buildings", "Tools", "Furniture"]),
            "supplier": fake.company(),
            "purchase_price": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "last_maintenance": fake.date_this_year(),
            "next_maintenance": fake.date_this_year(),
            "usage_hours": random.randint(0, 10000),
            "asset_condition": random.choice(["New", "Good", "Fair", "Poor"]),
            "insurance_policy": fake.bothify("POL-####-###"),
            "insurance_expiration": fake.date_this_decade()
        })
    
    return pd.DataFrame(data)

# Example usage:
df = generate_asset_management_data(10)
print(df.head())
