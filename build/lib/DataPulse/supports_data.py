from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate sports data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        score_team_1 = random.randint(0, 10)
        score_team_2 = random.randint(0, 10)

        # Determine the winner based on the scores
        if score_team_1 > score_team_2:
            winner = "Team 1"
        elif score_team_1 < score_team_2:
            winner = "Team 2"
        else:
            winner = "Draw"

        data.append({
            "match_id": str(fake.uuid4()),
            "sport_type": random.choice(["Football", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey", "Soccer", "Rugby"]),
            "team_1": fake.company(),
            "team_2": fake.company(),
            "match_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "match_location": fake.city(),
            "score_team_1": score_team_1,
            "score_team_2": score_team_2,
            "winner": winner,
            "referee_name": fake.name(),
            "duration": random.randint(60, 180),
            "tournament_name": fake.catch_phrase(),
            "player_of_the_match": fake.name(),
            "attendance": random.randint(1000, 50000),
            "ticket_price": round(random.uniform(5, 500), 2),
            "weather_conditions": random.choice(["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]),
            "broadcast_channel": fake.company(),
            "sponsor_name": fake.company(),
            "injury_report": random.choice(["None", "Minor", "Severe"]),
            "match_status": random.choice(["Completed", "Ongoing", "Scheduled"]),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_sports_data')
# def download_sports_data():
#     df = generate_sports_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="sports_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_sports_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
