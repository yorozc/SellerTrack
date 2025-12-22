# calculates sum for listed prices

def calc_price_sum(prices: list) -> float:
    sum = 0
    for price in prices:
        sum += price
    return sum