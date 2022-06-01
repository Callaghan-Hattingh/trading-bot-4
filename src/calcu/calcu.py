from src.api import get_trade_hist, get_all_open_orders, get_order_history_detail


def cal_buys(price: int) -> list[int]:
    l = []
    v = price - price % 5000
    for i in enumerate(range(v, 0, -5000)):
        if i[0] > 9:
            break
        l.append(i[1])
    return l


def int_to_customer_id_list(l: list[int]) -> list[str]:
    id_list = []
    for i in l:
        id_list.append(f"BTCZAR-{i}")
    return id_list


def check_if_buy_possible(customer_id: str) -> bool:
    h = get_order_history_detail(customer_id=customer_id)
    if not h:
        return True
    else:
        for i in h:
            if i["failedReason"] == "":
                if i["orderStatusType"] == "Cancelled" and i["orderSide"] == "buy":
                    return True
                elif i["orderStatusType"] == "Filled" and i["orderSide"] == "sell":
                    return True
                elif i["orderStatusType"] == "Cancelled" and i["orderSide"] == "sell":
                    return False
                elif i["orderStatusType"] == "Filled" and i["orderSide"] == "buy":
                    return False
                elif i["orderStatusType"] == "Placed" and i["orderSide"] == "buy":
                    return False
                elif i["orderStatusType"] == "Placed" and i["orderSide"] == "sell":
                    return False
                elif i["orderStatusType"] == "PartiallyFilled":
                    return False
                else:
                    return False


def check_if_sell_possible(customer_id: str) -> bool:
    h = get_order_history_detail(customer_id=customer_id)
    if not h:
        return False
    else:
        for i in h:
            if i["failedReason"] == "":
                if i["orderStatusType"] == "Cancelled" and i["orderSide"] == "buy":
                    return False
                elif i["orderStatusType"] == "Filled" and i["orderSide"] == "sell":
                    return False
                elif i["orderStatusType"] == "Cancelled" and i["orderSide"] == "sell":
                    return True
                elif i["orderStatusType"] == "Filled" and i["orderSide"] == "buy":
                    return True
                elif i["orderStatusType"] == "Placed" and i["orderSide"] == "buy":
                    return False
                elif i["orderStatusType"] == "Placed" and i["orderSide"] == "sell":
                    return False
                elif i["orderStatusType"] == "PartiallyFilled":
                    return False
                else:
                    return False


last_price = int(get_trade_hist().json()[0]["price"]) - 1 - 200000
buy_list = cal_buys(last_price)
buy_list_id = int_to_customer_id_list(buy_list)
open_orders = get_all_open_orders()

if __name__ == "__main__":
    # print(last_price)
    # print(buy_list)
    check_if_buy_possible(customer_id="BTCZAR-10001")
    # check_if_buy_possible(customer_id="test-1")


