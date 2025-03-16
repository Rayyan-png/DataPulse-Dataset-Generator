from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_transaction_id():
    return fake.uuid4()

def generate_customer_id():
    return fake.uuid4()

def generate_transaction_date():
    return fake.date_this_year()

def generate_transaction_amount():
    return round(fake.pydecimal(left_digits=5, right_digits=2, positive=True), 2)

def generate_transaction_type():
    return fake.random_element(elements=["Online", "In-Store", "ATM", "Wire Transfer"])

def generate_transaction_status():
    return fake.random_element(elements=["Success", "Failed", "Pending"])

def generate_payment_method():
    return fake.random_element(elements=["Credit Card", "Debit Card", "Bank Transfer", "Cryptocurrency"])

def generate_location():
    return fake.city()

def generate_ip_address():
    return fake.ipv4()

def generate_device_type():
    return fake.random_element(elements=["Mobile", "Desktop", "Tablet"])

def generate_merchant_name():
    return fake.company()

def generate_fraud_score():
    return round(fake.pyfloat(min_value=0, max_value=1), 2)

def generate_alert_flag():
    return fake.boolean(chance_of_getting_true=10)

def generate_currency():
    return fake.currency_code()

def generate_refund_status():
    return fake.random_element(elements=["None", "Partial", "Full"])

def generate_bank_name():
    return fake.company()

def generate_fraud_detection_data(num_records=100):
    data = [{
        "transaction_id": generate_transaction_id(),
        "customer_id": generate_customer_id(),
        "transaction_date": generate_transaction_date(),
        "transaction_amount": generate_transaction_amount(),
        "transaction_type": generate_transaction_type(),
        "transaction_status": generate_transaction_status(),
        "payment_method": generate_payment_method(),
        "location": generate_location(),
        "ip_address": generate_ip_address(),
        "device_type": generate_device_type(),
        "merchant_name": generate_merchant_name(),
        "fraud_score": generate_fraud_score(),
        "alert_flag": generate_alert_flag(),
        "currency": generate_currency(),
        "refund_status": generate_refund_status(),
        "bank_name": generate_bank_name()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_fraud_detection_data')
# def download_fraud_detection_data():
#     df = generate_fraud_detection_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='fraud_detection_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_fraud_detection_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)