from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate IT infrastructure data
def generate_it_infrastructure_data(num_records=100):
    data = []
    for _ in range(num_records):
        last_update = fake.date_time_this_year()
        contract_expiry = fake.date_this_decade()

        data.append({
            "device_id": str(fake.uuid4()),  # Ensure UUID is a string
            "device_type": random.choice(["Router", "Switch", "Firewall", "Server", "Storage", "Access Point"]),
            "ip_address": fake.ipv4(),
            "mac_address": fake.mac_address(),
            "os_version": random.choice(["Windows Server 2022", "Ubuntu 20.04", "CentOS 8", "Cisco IOS 15.2", "VMware ESXi 7.0"]),
            "location": f"{fake.city()}, {fake.country()}",
            "status": random.choice(["Active", "Inactive", "Maintenance", "Decommissioned"]),
            "last_update": last_update.strftime("%Y-%m-%d %H:%M:%S"),
            "owner_name": fake.name(),
            "serial_number": fake.bothify("SN-####-????"),
            "rack_location": fake.bothify("R##-U##"),
            "power_consumption": round(random.uniform(10.0, 500.0), 2),  # Limited power range
            "uptime": random.randint(0, 365),
            "network_speed": random.choice(["1Gbps", "10Gbps", "40Gbps", "100Gbps"]),
            "firmware_version": random.choice(["v1.0.3", "v2.2.1", "v3.1.4", "v4.0.2"]),
            "device_role": random.choice(["Core", "Distribution", "Access", "Edge"]),
            "security_level": random.choice(["High", "Medium", "Low"]),
            "contract_expiry": contract_expiry.strftime("%Y-%m-%d")
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_it_infrastructure_data')
# def download_it_infrastructure_data():
#     df = generate_it_infrastructure_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="it_infrastructure_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_it_infrastructure_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
