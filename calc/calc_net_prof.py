# calculates net_profit

def calc_net_prof(price: float, cost: float, shipping: float, fee_percent: float) -> float:
    return price - (cost + shipping + (price * (fee_percent / 100)))