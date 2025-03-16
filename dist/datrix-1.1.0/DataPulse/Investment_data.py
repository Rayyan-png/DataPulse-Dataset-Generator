from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate Investment Data
def generate_investment_data(num_records=100):
    data = []
    for _ in range(num_records):
        investment_date = fake.date_between(start_date="-5y", end_date="today")
        maturity_date = fake.date_between(start_date="today", end_date="+10y")

        data.append({
            "investment_id": str(fake.uuid4()),  # Ensure UUID is a string
            "investor_name": fake.name(),
            "investment_type": random.choice(["Stocks", "Bonds", "Real Estate", "Cryptocurrency", "Mutual Funds", "Commodities"]),
            "investment_amount": round(random.uniform(1000, 10000000), 2),  # Efficient random float range
            "currency": fake.currency_code(),
            "investment_date": investment_date.strftime("%Y-%m-%d"),  # Format date properly
            "maturity_date": maturity_date.strftime("%Y-%m-%d"),
            "risk_level": random.choice(["Low", "Medium", "High", "Very High"]),
            "return_rate": round(random.uniform(1, 20), 2),  # Return rate in percentage
            "broker_name": fake.company(),
            "investment_status": random.choice(["Active", "Closed", "Pending", "Withdrawn"]),
            "account_id": fake.bothify("ACCT-####-????"),
            "portfolio_id": fake.bothify("PORT-####"),
            "market_sector": random.choice(["Technology", "Healthcare", "Finance", "Energy", "Consumer Goods"]),
            "dividends": round(random.uniform(0, 50000), 2),  # Dividends in USD
            "tax_rate": round(random.uniform(0, 0.5), 2),  # Tax rate in percentage
            "advisor_name": fake.name(),
            "geographical_region": fake.country(),
            "transaction_fee": round(random.uniform(0, 5000), 2),  # Transaction fees
            "investment_strategy": random.choice(["Growth", "Income", "Value", "Balanced", "Aggressive"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_investment_data')
# def download_investment_data():
#     df = generate_investment_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="investment_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_investment_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
