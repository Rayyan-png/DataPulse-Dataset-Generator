from faker import Faker
import pandas as pd
from flask import Flask, send_file

fake = Faker()

app = Flask(__name__)

def generate_data(num_records=100):
    data = [
        {
            "purchase_order_id": fake.uuid4(),
            "supplier_name": fake.company(),
            "product_name": fake.word(),
            "quantity": fake.random_int(min=1, max=500),
            "unit_price": round(fake.random_number(digits=3) + fake.random_number(digits=2) / 100, 2),
            "total_cost": round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2),
            "order_date": fake.date_this_year(),
            "delivery_date": fake.date_between(start_date="today", end_date="+30d"),
            "order_status": fake.random_element(elements=["Pending", "Shipped", "Delivered", "Cancelled"]),
            "payment_status": fake.random_element(elements=["Paid", "Unpaid", "Partially Paid"])
        } 
        for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# @app.route('/download_purchase_order_data')
# def download_purchase_order_data():
#     df = generate_purchase_order_data(500000)
#     file_path = "purchase_order_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
