from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate cybersecurity incident dataset
def generate_cybersecurity_data(num_records=100):
    data = [{
        "incident_id": str(fake.uuid4()),
        "incident_type": random.choice(["Phishing", "Malware", "Data Breach", "DDoS", "Ransomware"]),
        "incident_date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
        "severity_level": random.choice(["Low", "Medium", "High", "Critical"]),
        "source_ip": fake.ipv4(),
        "destination_ip": fake.ipv4(),
        "attack_vector": random.choice(["Email", "Network", "Application", "Physical Access"]),
        "compromised_system": random.choice(["Database Server", "Web Server", "User Workstation", "Mobile Device"]),
        "detection_method": random.choice(["Firewall", "IDS/IPS", "User Report", "SIEM"]),
        "response_action": random.choice(["Isolated", "Patched", "Monitored", "No Action"]),
        "affected_department": random.choice(["IT", "Finance", "HR", "Marketing"]),
        "exfiltrated_data_size": f"{random.randint(1, 100)} MB",
        "malware_family": random.choice(["Trojan", "Worm", "Ransomware", "Spyware"]),
        "patch_status": random.choice(["Patched", "Unpatched", "Pending"]),
        "reported_by": fake.name(),
        "incident_duration": f"{random.randint(1, 72)} hours",
        "risk_score": round(random.uniform(0, 10), 1),
        "attack_motivation": random.choice(["Financial Gain", "Espionage", "Revenge", "Accidental"]),
        "data_encrypted": random.choice([True, False]),
        "threat_actor_type": random.choice(["Internal", "External", "Third-party"]),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_cybersecurity_data')
# def download_cybersecurity_data():
#     df = generate_cybersecurity_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="cybersecurity_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
