from faker import Faker
import pandas as pd
import random
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_banking_transaction_data(num_records=100):
    data = [{
        "transaction_id": str(fake.uuid4()),  # Ensure UUID is a string
        "account_number": fake.iban(),
        "transaction_date": fake.date_time_this_year(),
        "amount": round(float(fake.pydecimal(left_digits=6, right_digits=2, positive=True)), 2),
        "currency": fake.currency_code(),
        "transaction_type": random.choice(["Deposit", "Withdrawal", "Transfer", "Payment"]),
        "account_balance": round(float(fake.pydecimal(left_digits=7, right_digits=2, positive=True)), 2),
        "customer_id": str(fake.uuid4()),
        "branch_code": fake.random_number(digits=5, fix_len=True),
        "transaction_status": random.choice(["Completed", "Pending", "Failed"]),
        "merchant_name": fake.company(),
        "payment_method": random.choice(["Online", "ATM", "In-Branch", "Mobile"]),
        "card_number": fake.credit_card_number(),
        "card_type": fake.credit_card_provider(),
        "authorization_code": fake.bothify(text='??###-###'),
        "reference_number": fake.bothify(text='?????-#####'),
        "customer_name": fake.name(),
        "customer_email": fake.email(),
        "fraud_flag": fake.boolean(chance_of_getting_true=5),
        "fee_amount": round(float(fake.pydecimal(left_digits=3, right_digits=2, positive=True)), 2),
        "exchange_rate": round(random.uniform(0.5, 2.0), 4)  # Simulated realistic exchange rate
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Sample Data Display
if __name__ == '__main__':
    sample_df = generate_banking_transaction_data(10)
    print(sample_df.head(10))
    
    # app.run(debug=True)  # Uncomment if you want to run the Flask app

# Flask app for CSV download
# @app.route('/download_banking_transaction_data')
# def download_banking_transaction_data():
#     df = generate_banking_transaction_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='banking_transaction_data.csv')
