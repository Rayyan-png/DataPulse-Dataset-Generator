import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "transaction_id": fake.uuid4(),
            "amount": round(random.uniform(10, 10000), 2),
            "currency": fake.currency_code(),
            "transaction_date": fake.date_time_this_year(),
            "payment_method": random.choice(["Credit Card", "Debit Card", "Bank Transfer"]),
            "account_number": fake.iban(),
            "customer_id": fake.uuid4(),
            "merchant_name": fake.company(),
            "transaction_status": random.choice(["Completed", "Pending", "Failed"]),
            "country": fake.country(),
            "city": fake.city(),
            "zip_code": fake.zipcode(),
            "reference_number": fake.bothify("??###-###"),
            "card_type": fake.credit_card_provider(),
            "card_expiry": fake.credit_card_expire(),
            "fraud_flag": random.choice([True, False]),
            "exchange_rate": round(random.uniform(0.5, 1.5), 4),
            "fee_amount": round(random.uniform(1, 50), 2),
            "refund_status": random.choice(["None", "Partial", "Full"]),
            "branch_code": random.randint(10000, 99999),
        })
    
    return pd.DataFrame(data)

# Generate sample data
df_sample = generate_data(10)
print(df_sample.head())
