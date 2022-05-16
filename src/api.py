import requests
import time
from src.auth import sign_request
from dotenv import load_dotenv
import os
import json

load_dotenv()


def get_all_open_orders():
    timestamp = int(time.time() * 1000)
    verb = "GET"
    path = "/v1/orders/open"
    signature = sign_request(timestamp, verb, path)

    url = f"{os.getenv('ROOT_URL')}{path}"
    payload = {}
    headers = {
        "X-VALR-API-KEY": os.getenv("API_KEY"),
        "X-VALR-SIGNATURE": f"{signature}",
        "X-VALR-TIMESTAMP": f"{timestamp}",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def post_limit_order(
    side: str,
    amount: float,
    price: int,
    customer_id: str = None,
    *,
    pair: str = "BTCZAR",
    post_type: bool = True,
):
    timestamp = int(time.time() * 1000)
    verb = "POST"
    path = "/v1/orders/limit"

    url = f"{os.getenv('ROOT_URL')}{path}"
    payload = json.dumps({
        "side": side,
        "quantity": amount,
        "price": price,
        "pair": pair,
        "postOnly": post_type,
        'customerOrderId': customer_id,
    })
    signature = sign_request(timestamp, verb, path, body=payload)
    headers = {
        "X-VALR-API-KEY": os.getenv("API_KEY"),
        "X-VALR-SIGNATURE": f"{signature}",
        "X-VALR-TIMESTAMP": f"{timestamp}",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def del_order(*, pair: str = "BTCZAR", customer_id: str = None, order_id: str = None):
    timestamp = int(time.time() * 1000)
    verb = "DELETE"
    path = "/v1/orders/order"

    url = f"{os.getenv('ROOT_URL')}{path}"

    if customer_id is not None:
        payload = json.dumps({"customerOrderId": customer_id, "pair": pair})
    elif order_id is not None:
        payload = json.dumps({"orderId": order_id, "pair": pair})
    else:
        raise ValueError("Must provide either customer_id or order_id")

    signature = sign_request(timestamp, verb, path, body=payload)
    headers = {
        "X-VALR-API-KEY": os.getenv("API_KEY"),
        "X-VALR-SIGNATURE": f"{signature}",
        "X-VALR-TIMESTAMP": f"{timestamp}",
        "Content-Type": "application/json",
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response


def get_trade_hist(*, pair: str = "BTCZAR",skip: int = 0, limit: int = 1):
    timestamp = int(time.time() * 1000)
    verb = "GET"
    path = f"/v1/marketdata/{pair}/tradehistory?skip={skip}&limit={limit}"

    url = f"{os.getenv('ROOT_URL')}{path}"
    payload = {}
    signature = sign_request(timestamp, verb, path)
    headers = {
        "X-VALR-API-KEY": os.getenv("API_KEY"),
        "X-VALR-SIGNATURE": f"{signature}",
        "X-VALR-TIMESTAMP": f"{timestamp}",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def get_order_history_summary(*, pair: str = "BTCZAR", customer_id: str = None, order_id: str = None):
    if customer_id is not None:
        path = f"/v1/orders/history/{customer_id}?pair={pair}"
    elif order_id is not None:
        path = f"/v1/orders/history/{order_id}?pair={pair}"
    else:
        raise ValueError("Must provide either customer_id or order_id")




if __name__ == "__main__":
    w = (get_trade_hist())
    print(w.text)

    y = get_all_open_orders()
    y = y.json()
    for i in y:
        print(i)
    x = post_limit_order("BUY", 0.00100000, 10001, 'BTCZAR-10001')
    # q = del_order(customer_id='BTCZAR-10001')
    # print(q)
    # print(x.text)
    # print(x.status_code)
