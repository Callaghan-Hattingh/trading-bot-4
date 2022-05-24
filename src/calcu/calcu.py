from src.api import get_trade_hist, get_all_open_orders, get_order_history_detail


def cal_buys(price: int):
    l = []
    v = price - price % 5000
    for i in enumerate(range(v, 0, -5000)):
        if i[0] > 9:
            break
        l.append(i[1])
    return l


last_price = int(get_trade_hist().json()[0]["price"]) - 1 - 200000
buy_list = cal_buys(last_price)
open_orders = get_all_open_orders()

if __name__ == "__main__":
    print(last_price)
    print(buy_list)
    print(open_orders.json())
