from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate genomic data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "sample_id": str(fake.uuid4()),  # Ensure UUID is a string
            "gene_sequence": ''.join(random.choices("ATCG", k=100)),  # Generate a 100-base sequence
            "gene_name": fake.bothify(text='GENE-###'),
            "mutation_type": random.choice(["Insertion", "Deletion", "Substitution", "Duplication", "Inversion"]),
            "chromosome_number": random.randint(1, 23),
            "position": random.randint(1000, 1000000),
            "genotype": random.choice(["AA", "AT", "TT", "CC", "GG", "AG"]),
            "expression_level": round(random.uniform(0.001, 99.999), 3),
            "variation_frequency": round(random.uniform(0.00001, 1.0), 5),
            "disease_association": random.choice(["Cancer", "Diabetes", "Alzheimer's", "Cardiovascular", "None"]),
            "sample_source": random.choice(["Blood", "Saliva", "Tissue", "Buccal Swab"]),
            "reference_genome": random.choice(["GRCh37", "GRCh38", "hg19", "hg38"]),
            "gene_family": random.choice(["Kinase", "Homeobox", "Zinc Finger", "Immunoglobulin"]),
            "transcription_factor": random.choice(["TP53", "MYC", "SOX2", "PAX6"]),
            "snp_id": fake.bothify(text='rs#####'),
            "allele_frequency": round(random.uniform(0.000001, 1.0), 6),
            "methylation_level": round(random.uniform(0.01, 100.0), 2),
            "exon_number": random.randint(1, 50),
            "pathogenicity_score": round(random.uniform(0.0001, 1.0), 4),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_genomic_data')
# def download_genomic_data():
#     df = generate_genomic_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="genomic_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_genomic_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
