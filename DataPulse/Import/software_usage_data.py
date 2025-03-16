from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_user_id():
    return fake.uuid4()

def generate_user_name():
    return fake.user_name()

def generate_email():
    return fake.email()

def generate_ip_address():
    return fake.ipv4()

def generate_device_type():
    return fake.random_element(elements=["Desktop", "Laptop", "Tablet", "Mobile"])

def generate_browser():
    return fake.random_element(elements=["Chrome", "Firefox", "Safari", "Edge", "Opera"])

def generate_os():
    return fake.random_element(elements=["Windows", "macOS", "Linux", "Android", "iOS"])

def generate_login_time():
    return fake.date_time_this_year()

def generate_logout_time():
    return fake.date_time_this_year()

def generate_action_performed():
    return fake.random_element(elements=["Login", "Logout", "File Upload", "Download", "Edit", "Delete"])

def generate_page_visited():
    return fake.uri_path()

def generate_error_code():
    return fake.random_element(elements=["200", "404", "500", "403", "401"])

def generate_session_duration():
    return fake.random_int(min=1, max=3600)

def generate_license_key():
    return fake.bothify("????-####-????-####")

def generate_feature_used():
    return fake.random_element(elements=["Dashboard", "Reports", "User Management", "Settings", "API Access"])

def generate_subscription_type():
    return fake.random_element(elements=["Free", "Basic", "Pro", "Enterprise"])

def generate_software_version():
    return fake.random_element(elements=["1.0", "2.1", "3.5", "4.2", "5.0"])

def generate_bug_reported():
    return fake.boolean(chance_of_getting_true=5)

def generate_feedback_score():
    return fake.random_int(min=1, max=10)

def generate_software_usage_data(num_records=100):
    data = [{
        "user_id": generate_user_id(),
        "user_name": generate_user_name(),
        "email": generate_email(),
        "ip_address": generate_ip_address(),
        "device_type": generate_device_type(),
        "browser": generate_browser(),
        "os": generate_os(),
        "login_time": generate_login_time(),
        "logout_time": generate_logout_time(),
        "action_performed": generate_action_performed(),
        "page_visited": generate_page_visited(),
        "error_code": generate_error_code(),
        "session_duration": generate_session_duration(),
        "license_key": generate_license_key(),
        "feature_used": generate_feature_used(),
        "subscription_type": generate_subscription_type(),
        "software_version": generate_software_version(),
        "bug_reported": generate_bug_reported(),
        "feedback_score": generate_feedback_score()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_software_usage_data')
# def download_software_usage_data():
#     df = generate_software_usage_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='software_usage_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_software_usage_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
