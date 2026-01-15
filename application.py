from calc.calc_net_prof import calc_net_prof
from calc.calc_price_sum import calc_price_sum
from calc.calc_total_sum import calc_netprof_sum
from domain.item import Item #item object
import csv
import os
import pandas as pd

# TODO: add error handling

def create_item(name: str, price: float, og_price: float) -> Item:
    new_item = Item(name, price, og_price)
    save_item(new_item)
    print("================\nItem Added!\n================\n")
    return new_item

def save_item(item: Item): # write to csv
    with open('data/items_file.csv', mode='a') as items_file:
        fieldnames = ['name', 'price', 'og_price', 'profit']
        writer = csv.DictWriter(items_file, fieldnames=fieldnames)
        if items_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'name': item.name, 'price': item.price, 'og_price':item.og_price, 'profit': item.price - item.og_price})
       
def delete_item(key: str):
    item = search_item(key)
    if item:
        pass
    else:
        return

def search_item(key: str) -> Item:
    with open('data/items_file.csv', 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            if key in line:
                 key_item = Item(line[0], float(line[1]), float(line[2]))
                 print(f'\n{key_item}\n')
                 return key_item
            
        print('\nItem not Found!\n')
        return None

def display_items():
    if os.path.isfile('data/items_file.csv'):
        print()
        print(pd.read_csv('data/items_file.csv'))
        print()
                
    else:
        print("FILE NOT FOUND.")

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