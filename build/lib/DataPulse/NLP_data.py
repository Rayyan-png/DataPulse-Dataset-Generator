from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate NLP text data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        publication_date = fake.date_between(start_date='-5y', end_date='today')

        data.append({
            "document_id": str(fake.uuid4()),
            "text_snippet": fake.text(max_nb_chars=200),
            "sentiment": random.choice(["Positive", "Negative", "Neutral"]),
            "language": random.choice(["English", "Spanish", "French", "German", "Chinese", "Japanese", "Arabic"]),
            "author": fake.name(),
            "publication_date": publication_date.strftime("%Y-%m-%d"),
            "topic": random.choice(["Technology", "Health", "Finance", "Education", "Entertainment", "Politics", "Science"]),
            "text_length": random.randint(50, 10000),
            "document_type": random.choice(["Article", "Review", "Report", "Essay", "Blog Post", "Speech", "Transcript"]),
            "summary": fake.text(max_nb_chars=300),
            "keyword": fake.word(),
            "readability_score": round(random.uniform(0.0, 100.0), 1),  # Ensuring a valid readability score
            "sentiment_score": round(random.uniform(-1.0, 1.0), 2),  # Ensuring sentiment scores in range [-1, 1]
            "text_source": random.choice(["News Website", "Social Media", "Journal", "Blog", "Corporate Report"]),
            "entity_count": random.randint(0, 50),
            "named_entities": [fake.company() for _ in range(random.randint(1, 5))],  # Ensuring realistic entity lists
            "emotion": random.choice(["Joy", "Sadness", "Anger", "Surprise", "Fear", "Neutral"]),
            "language_model": random.choice(["BERT", "GPT", "RoBERTa", "XLNet", "T5"]),
            "translation": fake.text(max_nb_chars=150),
            "source_url": fake.url()
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_nlp_data')
# def download_nlp_data():
#     df = generate_nlp_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="nlp_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_nlp_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
