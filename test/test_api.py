from src.api import get_all_open_orders, post_limit_order, del_order


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
