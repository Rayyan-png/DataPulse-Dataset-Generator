from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "order_id": fake.uuid4(),
            "customer_id": fake.uuid4(),
            "order_date": fake.date_this_year(),
            "order_status": random.choice(["Pending", "Shipped", "Delivered", "Cancelled"]),
            "total_amount": round(random.uniform(10, 5000), 2),
            "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]),
            "shipping_address": fake.address(),
            "billing_address": fake.address(),
            "delivery_date": fake.date_between(start_date="-30d", end_date="today"),
            "order_notes": fake.sentence(),
        })
    
    return pd.DataFrame(data)

# Generate sample data
df_sample = generate_data(10)
print(df_sample.head())
