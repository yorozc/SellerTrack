# calculates sum of net profit

def calc_netprof_sum(netprof: list) -> float:
    sum = 0
    for money in netprof:
        sum += money 
    return sum