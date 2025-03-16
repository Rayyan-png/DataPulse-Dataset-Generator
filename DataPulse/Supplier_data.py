from faker import Faker
import pandas as pd

def generate_data(num_records=100):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        data.append({
            "supplier_id": fake.uuid4(),
            "company_name": fake.company(),
            "contact_name": fake.name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "address": fake.address(),
            "city": fake.city(),
            "country": fake.country(),
            "postal_code": fake.postcode(),
            "website": fake.url(),
            "product_category": fake.random_element(elements=["Electronics", "Clothing", "Groceries", "Furniture", "Pharmaceuticals"]),
            "contract_start_date": fake.date_this_decade(),
            "contract_end_date": fake.date_this_decade() if fake.boolean(chance_of_getting_true=70) else None,
            "payment_terms": fake.random_element(elements=["Net 30", "Net 60", "Net 90"]),
            "rating": fake.random_int(min=1, max=5),
        })
    
    return pd.DataFrame(data)

# Generate sample supplier data
df_sample = generate_data(10)
print(df_sample.head())
