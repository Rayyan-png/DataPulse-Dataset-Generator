from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_voter_id():
    return fake.uuid4()

def generate_voter_name():
    return fake.name()

def generate_age():
    return fake.random_int(min=18, max=90)

def generate_gender():
    return fake.random_element(elements=["Male", "Female", "Non-Binary", "Other"])

def generate_voting_district():
    return fake.city()

def generate_party_affiliation():
    return fake.random_element(elements=["Independent", "Democratic", "Republican", "Green", "Libertarian"])

def generate_vote_status():
    return fake.random_element(elements=["Voted", "Not Voted", "Pending"])

def generate_ballot_type():
    return fake.random_element(elements=["In-person", "Mail-in", "Absentee"])

def generate_registration_date():
    return fake.date_this_decade()

def generate_polling_station():
    return fake.street_address()

def generate_election_type():
    return fake.random_element(elements=["Local", "State", "Federal", "Presidential"])

def generate_vote_time():
    return fake.date_time_this_year()

def generate_voting_and_election_data(num_records=100):
    data = [{
        "voter_id": generate_voter_id(),
        "voter_name": generate_voter_name(),
        "age": generate_age(),
        "gender": generate_gender(),
        "voting_district": generate_voting_district(),
        "party_affiliation": generate_party_affiliation(),
        "vote_status": generate_vote_status(),
        "ballot_type": generate_ballot_type(),
        "registration_date": generate_registration_date(),
        "polling_station": generate_polling_station(),
        "election_type": generate_election_type(),
        "vote_time": generate_vote_time()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_voting_and_election_data')
# def download_voting_and_election_data():
#     df = generate_voting_and_election_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='voting_and_election_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_voting_and_election_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
