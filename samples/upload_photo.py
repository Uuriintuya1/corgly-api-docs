import os
import requests

auth_token = os.environ["CORGLY_TOKEN"]

with open("einstein.jpg", "rb") as photo_file:
    upload_response = requests.post(
        "https://api.corg.ly/v1/pets/upload-photo",
        headers={"Authorization": f"Bearer {auth_token}"},
        data={"pet_id": "corgi_98231"},
        files={"photo": photo_file},
    )

print(upload_response.status_code)