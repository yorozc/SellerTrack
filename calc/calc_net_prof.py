# calculates net_profit

def calc_net_prof(profit: float, shipping: float, fee_percent: float) -> float:
    return profit - shipping - (profit * fee_percent)