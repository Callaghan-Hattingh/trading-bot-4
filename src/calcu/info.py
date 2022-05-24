from src.api import get_trade_hist
from src.calcu.calcu import last_price, open_orders, buy_list


def open_orders_customer_id(open_orders):
    return [order['customerOrderId'] for order in open_orders]



def open_buy_orders(open_orders):
    """
    Returns a list of buy orders.
    """
    return [order for order in open_orders if order['side'] == "buy"]


def open_sell_orders(open_orders):
    """
    Returns a list of sell orders.
    """
    return [order for order in open_orders if order['side'] == "sell"]


def open_orders_to_delete_buy(open_buy_orders, buy_list):
    # buy_list - open_buy_orders
    #
    pass


def open_orders_to_create_buy(open_buy_orders, buy_list):
    pass


def open_orders_to_delete_sell():
    pass


def open_orders_to_create_sell():
    pass


if __name__ == "__main__":
    print(last_price)
    print(open_orders)
    print(buy_list)
    print(open_buy_orders(open_orders))
    # print(open_sell_orders(open_orders))