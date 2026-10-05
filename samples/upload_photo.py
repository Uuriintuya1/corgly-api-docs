import os
import requests

# Registers your server URL to receive pet activity events.
# Replace callback_url with a public HTTPS endpoint you own.
auth_token = os.environ["CORGLY_TOKEN"]

subscription_response = requests.post(
    "https://api.corg.ly/v1/webhooks/subscribe",
    headers={"Authorization": f"Bearer {auth_token}"},
    json={
        "callback_url": "https://your-app.example.com/hooks/corgly",
        "events": ["bark.detected", "photo.uploaded"],
    },
)

print(subscription_response.status_code, subscription_response.json())