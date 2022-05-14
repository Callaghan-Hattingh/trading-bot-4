import time
import hashlib
import hmac


def sign_request(api_key_secret, timestamp, verb, path, body=""):
    """Signs the request payload using the api key secret
    api_key_secret - the api key secret
    timestamp - the unix timestamp of this request e.g. int(time.time()*1000)
    verb - Http verb - GET, POST, PUT or DELETE
    path - path excluding host name, e.g. '/v1/withdraw
    body - http request body as a string, optional
    """
    payload = "{}{}{}{}".format(timestamp, verb.upper(), path, body)
    message = bytearray(payload, "utf-8")
    signature = hmac.new(
        bytearray(api_key_secret, "utf-8"), message, digestmod=hashlib.sha512
    ).hexdigest()
    return signature


if __name__ == "__main__":
    api_key_secret = "5a94dc2ae51fc0efce5476859100f202bf2c77c74829873d758c5c9c9f652a85"
    timestamp = int(time.time() * 1000)
    verb = "GET"
    path = "/v1/orders/open"
    body = ""
    signature = sign_request(api_key_secret, timestamp, verb, path, body)
    print(signature)

    import requests

    url = "https://api.valr.com/v1/orders/open"

    payload = {}
    headers = {
        'X-VALR-API-KEY': '009a2e4198c0953de7b985b8ae0bd620bc131638a857051fef1fa8214540fb23',
        'X-VALR-SIGNATURE': f'{signature}',
        'X-VALR-TIMESTAMP': f'{timestamp}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



