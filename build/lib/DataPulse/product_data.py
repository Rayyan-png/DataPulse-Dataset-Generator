import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "product_id": fake.uuid4(),
            "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
            "category": fake.random_element(["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Books"]),
            "price": round(random.uniform(5, 1000), 2),
            "stock_quantity": random.randint(1, 500),
            "supplier": fake.company(),
            "manufacture_date": fake.date_between(start_date='-2y', end_date='today'),
            "expiry_date": fake.date_between(start_date='today', end_date='+2y') if random.choice([True, False]) else None,
            "rating": round(random.uniform(1, 5), 1),
        })
    
    return pd.DataFrame(data)

# Generate and save the product data
df = generate_data(500)
df.to_csv("product_data.csv", index=False)

print("Product data CSV file has been generated successfully!")
