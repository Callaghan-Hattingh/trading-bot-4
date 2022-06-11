from src.calcu.info import buy_list_open_orders_to_delete, buy_list_orders_to_place
from src.calcu.calcu import open_orders, buy_list_id
from src.api import post_limit_order, del_order

def orders_delete():
    d = buy_list_open_orders_to_delete(open_orders, buy_list_id)
    if not d:
        return True
    else:
        for i in d:
            print(i)
            del_order(customer_id=i)
            pass
        return False
    pass


def orders_placed():
    buy_list_orders_to_place(buy_list_id)
    pass
