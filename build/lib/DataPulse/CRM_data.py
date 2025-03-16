from faker import Faker
import pandas as pd
from flask import Flask, send_file

fake = Faker()

app = Flask(__name__)

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "customer_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "company": fake.company(),
            "industry": fake.random_element(elements=["Retail", "Finance", "Healthcare", "Technology", "Education"]),
            "last_contact_date": fake.date_this_year(),
            "contact_method": fake.random_element(elements=["Email", "Phone", "In-Person", "Chatbot", "Social Media"]),
            "purchase_history": fake.random_int(min=0, max=20),
            "total_spent": round(fake.random_number(digits=5), 2),
            "customer_rating": round(fake.random_number(digits=1), 1),
            "loyalty_status": fake.random_element(elements=["Bronze", "Silver", "Gold", "Platinum"]),
            "preferred_product_category": fake.random_element(elements=["Electronics", "Clothing", "Home & Kitchen", "Books", "Health & Beauty"]),
            "feedback_score": fake.random_int(min=1, max=10),
            "next_followup_date": fake.date_between(start_date="today", end_date="+30d"),
            "assigned_sales_rep": fake.name()
        })
    return pd.DataFrame(data)

# @app.route('/download_crm_data')
# def download_crm_data():
#     df = generate_crm_data(5000)
#     file_path = "crm_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
