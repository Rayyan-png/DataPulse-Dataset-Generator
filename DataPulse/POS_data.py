from faker import Faker
import pandas as pd

def generate_data(num_records=100):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "transaction_id": fake.uuid4(),
            "store_id": fake.random_int(min=1000, max=9999),
            "cashier_id": fake.random_int(min=100, max=999),
            "customer_id": fake.uuid4(),
            "product_id": fake.uuid4(),
            "product_name": fake.word(),
            "category": fake.random_element(elements=["Electronics", "Clothing", "Groceries", "Home & Kitchen", "Toys", "Books"]),
            "quantity": fake.random_int(min=1, max=10),
            "price_per_unit": round(fake.random_number(digits=3) + fake.random_number(digits=2) / 100, 2),
            "total_price": round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2),
            "payment_method": fake.random_element(elements=["Credit Card", "Debit Card", "Cash", "Mobile Payment"]),
            "transaction_date": fake.date_this_year(),
            "transaction_time": fake.time(),
            "discount_applied": round(fake.random_number(digits=2) / 100, 2),
            "tax_amount": round(fake.random_number(digits=2) / 100, 2),
            "final_amount": round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2),
        }
        data.append(record)
    
    return pd.DataFrame(data)

# Generate sample POS data
df_sample = generate_data(10)
print(df_sample.head())

# Save to CSV
df_sample.to_csv("pos_data.csv", index=False)
