from faker import Faker
import pandas as pd

fake = Faker()

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "inventory_id": fake.uuid4(),
            "product_name": fake.word(),
            "product_category": fake.random_element(elements=["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]),
            "quantity_available": fake.random_int(min=0, max=1000),
            "warehouse_location": fake.city(),
            "supplier_name": fake.company(),
            "supplier_contact": fake.phone_number(),
            "last_restocked_date": fake.date_this_year(),
            "expiration_date": fake.date_between(start_date="+30d", end_date="+365d"),
            "cost_per_unit": round(fake.random_number(digits=3), 2),
            "selling_price": round(fake.random_number(digits=4), 2),
            "reorder_level": fake.random_int(min=10, max=500),
            "stock_status": fake.random_element(elements=["In Stock", "Out of Stock", "Low Stock"])
        })
    
    return pd.DataFrame(data)

# Generate sample data
df_sample = generate_data(10)
print(df_sample.head())

# Save as CSV
df_sample.to_csv("inventory_data.csv", index=False)
