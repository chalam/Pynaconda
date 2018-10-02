import sys
from src.data_structures.utils import make_arrary


def maximize_buy_low_sell_high(prices):
    min_price = sys.maxsize
    max_profit = 0
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        if max_profit < price-min_price:
            max_profit = price - min_price
            max_idx = i
        print(i, price, min_price, max_profit)
    return max_profit, max_idx

prices = [10, 7, 5, 8, 11, 9]
print(maximize_buy_low_sell_high(prices))

prices = make_arrary()
print(prices, maximize_buy_low_sell_high(prices))
