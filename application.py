from calc.calc_net_prof import calc_net_prof
from calc.calc_price_sum import calc_price_sum
from calc.calc_total_sum import calc_netprof_sum
from domain.item import Item #item object
import os.path
import csv



def create_item(name: str, price: float, og_price: float):
    new_item = Item(name, price, og_price)
    save_item(new_item)
    print("Item Added!")
    return new_item

def save_item(item: Item): # write to csv
    with open('data/items_file.csv', mode='a') as items_file:
        fieldnames = ['name', 'price', 'og_price', 'profit']
        writer = csv.DictWriter(items_file, fieldnames=fieldnames)
        if items_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'name': item.name, 'price': item.price, 'og_price':item.og_price, 'profit': item.price - item.og_price})
       

def delete_item(item: Item):
    pass

def search_item(key: str):
    pass

def display_items():
    with open('data/items_file.csv', mode='r') as items_file:
        pass

# def get_net_prof(profit, shipping, fee_percent):
#     return calc_net_prof(profit, shipping, fee_percent)

def get_net_prof_sum(items, shipping, fee_percent): # list of net profits for all items
    netprofits = []
    for item in items:
        profit = item.og_price - item.price
        netprofits.append(calc_net_prof(profit, shipping, fee_percent))
    return calc_netprof_sum(netprofits)

def get_price_sum(items: list):
    prices_list = []
    for item in items:
        prices += item.price
        prices_list.append(prices)
    return calc_price_sum(prices_list)