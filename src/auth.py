import os
import time
import hashlib
import hmac
from dotenv import load_dotenv

load_dotenv()


def sign_request(
    timestamp: int,
    verb: str,
    path: str,
    *,
    api_key_secret: str = os.getenv("API_SECRET"),
    body=""
):
    """Signs the request payload using the api key secret
    api - the api key secret
    t - the unix t of this request e.g. int(time.time()*1000)
    v - Http v - GET, POST, PUT or DELETE
    p - p excluding host name, e.g. '/v1/withdraw
    body - http request body as a string, optional
    """
    payload = "{}{}{}{}".format(timestamp, verb.upper(), path, body)
    message = bytearray(payload, "utf-8")
    signature = hmac.new(
        bytearray(api_key_secret, "utf-8"), message, digestmod=hashlib.sha512
    ).hexdigest()
    return signature


if __name__ == "__main__":
    s = sign_request(
        int(time.time() * 1000),
        "GET",
        "/v1/orders/open",
    )
    print(s)
