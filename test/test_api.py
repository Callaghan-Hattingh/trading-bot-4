import requests
import time
from src.auth import sign_request
from dotenv import load_dotenv
import os

load_dotenv()


def test_get_all_open_orders():
    timestamp = int(time.time() * 1000)
    verb = "GET"
    path = "/v1/orders/open"
    signature = sign_request(timestamp, verb, path)

    url = "https://api.valr.com/v1/orders/open"
    payload = {}
    headers = {
        "X-VALR-API-KEY": os.getenv("API_KEY"),
        "X-VALR-SIGNATURE": f"{signature}",
        "X-VALR-TIMESTAMP": f"{timestamp}",
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200


