from faker import Faker
import pandas as pd
from flask import Flask, send_file

fake = Faker()
app = Flask(__name__)

def generate_data(num_records=100):
    data = [
        {
            "invoice_id": fake.uuid4(),
            "customer_id": fake.uuid4(),
            "customer_name": fake.name(),
            "email": fake.email(),
            "billing_address": fake.address(),
            "invoice_date": fake.date_this_year(),
            "due_date": fake.date_this_year(),
            "total_amount": round(fake.random_number(digits=5), 2),
            "currency": fake.random_element(elements=["USD", "EUR", "GBP", "INR", "AUD"]),
            "payment_status": fake.random_element(elements=["Paid", "Pending", "Overdue"]),
            "payment_method": fake.random_element(elements=["Credit Card", "Bank Transfer", "PayPal", "Cash"]),
            "tax_amount": round(fake.random_number(digits=3), 2),
            "discount": round(fake.random_number(digits=2), 2),
            "net_amount": round(fake.random_number(digits=5), 2),
            "invoice_notes": fake.sentence(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# @app.route('/download_billing_invoicing_data')
# def download_billing_invoicing_data():
#     df = generate_billing_invoicing_data(5000)
#     file_path = "billing_invoicing_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
