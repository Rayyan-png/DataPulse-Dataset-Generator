from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate gaming data
def generate_gaming_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "game_id": str(fake.uuid4()),  # Ensure UUID is a string
            "player_id": str(fake.uuid4()),  # Ensure UUID is a string
            "player_username": fake.user_name(),
            "game_name": random.choice(["Battle Royale", "Space Quest", "Mystery Mansion", "Zombie Survival"]),
            "score": random.randint(0, 10000),
            "level_reached": random.randint(1, 50),
            "play_time": random.randint(5, 600),  # Play time in minutes
            "device_type": random.choice(["PC", "Console", "Mobile"]),
            "region": random.choice(["North America", "Europe", "Asia", "South America", "Australia"]),
            "in_game_purchases": random.choice([True, False]),  # Boolean value
            "achievement_unlocked": random.choice(["First Blood", "Speed Runner", "Treasure Hunter", "Master Strategist"]),
            "match_outcome": random.choice(["Win", "Lose", "Draw"]),
            "team_size": random.randint(1, 10),
            "match_duration": random.randint(5, 120),  # Duration in minutes
            "game_mode": random.choice(["Solo", "Duo", "Squad"]),
            "connection_type": random.choice(["Wi-Fi", "Ethernet", "5G"]),
            "event_participation": random.choice([True, False]),  # Boolean value
            "item_collected": random.choice(["Health Pack", "Rare Sword", "Magic Shield", "Power Boost"]),
            "chat_messages": fake.sentence(),
            "friends_count": random.randint(0, 500)
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_gaming_data')
# def download_gaming_data():
#     df = generate_gaming_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="gaming_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_gaming_data(10)
#     print(sample_df.head(10))  # Print sample data
#     app.run(debug=True)
