import os
import requests

# Sends a bark recording and prints its meaning.
# Assumes CORGLY_TOKEN is set and bark_001.wav exists locally.
auth_token = os.environ["CORGLY_TOKEN"]

with open("bark_001.wav", "rb") as bark_audio:
    bark_response = requests.post(
        "https://api.corg.ly/v1/audio/translate-bark",
        headers={"Authorization": f"Bearer {auth_token}"},
        data={"pet_id": "corgi_98231"},
        files={"audio": bark_audio},
    )

print(bark_response.status_code, bark_response.json()["translation"])