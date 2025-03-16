from faker import Faker
import pandas as pd
from flask import Flask, send_file
import io

fake = Faker()
app = Flask(__name__)

def generate_research_id():
    return fake.uuid4()

def generate_research_title():
    return fake.sentence(nb_words=6)

def generate_research_field():
    return fake.random_element(elements=["Physics", "Biology", "Computer Science", "Mathematics", "Medicine", "Social Sciences", "Engineering"])

def generate_researcher_name():
    return fake.name()

def generate_institution():
    return fake.company()

def generate_publication_date():
    return fake.date_this_decade()

def generate_funding_amount():
    return round(fake.pydecimal(left_digits=6, right_digits=2, positive=True), 2)

def generate_peer_review_status():
    return fake.random_element(elements=["Accepted", "In Review", "Rejected"])

def generate_citation_count():
    return fake.random_int(min=0, max=5000)

def generate_data_availability():
    return fake.random_element(elements=["Open Access", "Restricted", "Proprietary"])

def generate_ethics_approval():
    return fake.boolean(chance_of_getting_true=80)

def generate_research_summary():
    return fake.paragraph(nb_sentences=3)

def generate_collaborating_institutions():
    return fake.company()

def generate_academic_research_data(num_records=100):
    data = [{
        "research_id": generate_research_id(),
        "research_title": generate_research_title(),
        "research_field": generate_research_field(),
        "researcher_name": generate_researcher_name(),
        "institution": generate_institution(),
        "publication_date": generate_publication_date(),
        "funding_amount": generate_funding_amount(),
        "peer_review_status": generate_peer_review_status(),
        "citation_count": generate_citation_count(),
        "data_availability": generate_data_availability(),
        "ethics_approval": generate_ethics_approval(),
        "research_summary": generate_research_summary(),
        "collaborating_institutions": generate_collaborating_institutions()
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# @app.route('/download_academic_research_data')
# def download_academic_research_data():
#     df = generate_academic_research_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='academic_research_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_academic_research_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
