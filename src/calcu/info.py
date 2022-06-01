from src.api import get_trade_hist
from src.calcu.calcu import last_price, open_orders, buy_list, buy_list_id, check_if_buy_possible


def buy_list_open_orders_to_delete(open_orders, buy_list_id):
    d = []
    open_list = [
        order["customerOrderId"] for order in open_orders if order["side"] == "buy"
    ]
    del_list = [i in buy_list_id for i in open_list]
    for i in enumerate(del_list):
        if i[1]:
            pass
        elif not i[1]:
            d.append(open_list[i[0]])
    for i in enumerate(d):
        if int(i[1][7:]) > int(buy_list_id[0][7:]):
            d.pop(i[0])
    print(d)
    return d


def buy_list_orders_to_place(buy_list_id):
    b = []
    for i in buy_list_id:
        if check_if_buy_possible(customer_id=i):
            b.append(i)
    print(b)
    return b


if __name__ == "__main__":
    # print(last_price)
    # print(open_orders)
    # print(buy_list_id)
    buy_list_open_orders_to_delete(open_orders, buy_list_id)
    buy_list_orders_to_place(buy_list_id)
