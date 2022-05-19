from src.api import get_all_open_orders, post_limit_order, del_order
from src.auth import sign_request


def test_sign_request():
    response = sign_request(1652958074138, "GET", "/v1/orders/open")
    print(response)
    assert (
        "037220009189eda4fdd1a43fcc96f9bf642e1a93803de25746f3d1e73e37b908"
        "6513c07bcc94b99a2d570f1868cde670310160f48eda20b1b8cd75b6361150f8" == response
    )


def test_get_all_open_orders():
    response = get_all_open_orders()
    assert response.status_code == 200


def test_create_and_delete_post_order():
    # side = 'BUY'
    # amount = 0.001
    # price = 10000
    # custom_id = 'pytest-trading-bot-4'
    # create = post_limit_order(side, amount, price, custom_id)
    # delete = del_order(customer_id=custom_id)
    # print(1)
    # print(create.text)
    # print(2)
    # print(delete.text)
    # assert create.status_code == 200
    # assert delete.status_code == 200
    pass
