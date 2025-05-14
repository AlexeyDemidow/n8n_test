import os
from os.path import join, dirname

import requests
import json

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

test_url = os.environ.get("TEST_URL")
prod_url = os.environ.get("PROD_URL")
headers = {
    "Content-Type": "application/json"
}

data = {
    "name": "Анна",
    # "email": "bad",
    "email": "anna@mail.ru",
    "message": "Интересует Rolex Submariner"
}

response = requests.post(prod_url, headers=headers, data=json.dumps(data))  # Для тестов вставить test_url

print("Status code:", response.status_code)
print("Response body:", response.text)
