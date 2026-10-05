import os
import requests

auth_token = os.environ["CORGLY_TOKEN"]

subscription_response = requests.post(
    "https://api.corg.ly/v1/webhooks/subscribe",
    headers={"Authorization": f"Bearer {auth_token}"},
    json={
        "callback_url": "https://example.com/webhooks/corgly",
        "events": ["pet.updated", "bark.translated"],
    },
)

print(subscription_response.status_code)