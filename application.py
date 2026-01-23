from calc.calc_net_prof import calc_net_prof
from calc.calc_netprof_sum import calc_netprof_sum
from domain.item import Item #item object
import csv
import os
import pandas as pd

# TODO: add error handling

# helper func to just read csv file
def return_csv():
    pass

def create_item(name: str, price: float, og_price: float, shipping_fee: float, platform_fee: float) -> Item:
    new_item = Item(name.lower(), price, og_price, shipping_fee, platform_fee)
    save_item(new_item)
    print("================\nItem Added!\n================\n")
    return new_item

def save_item(item: Item): # write to csv
    # TODO: Add netprofit, shipping fee, other fees (seller fees like ebay or depop)
    with open('data/items_file.csv', mode='a') as items_file:
        fieldnames = ['name', 'price', 'og_price', 'profit', 'shipping', 'platform_fee']
        writer = csv.DictWriter(items_file, fieldnames=fieldnames)
        if items_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'name': item.name, 'price': item.price, 'og_price':item.og_price, 'profit': item.price - item.og_price,
                         'shipping': item.shipping, 'platform_fee': item.platform_fee})
       
def delete_item(search_term: str):
    item = search_item(search_term)
    items = {}
    if item: # if item found
        result_dict = {}
        with open('data/items_file.csv', mode='r') as file: # read into items dict
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                items[f"{lines['name']}"] = lines

            # delete item by adding not found items to dictionary
            for key, value in items.items():
                if search_term != key:
                    result_dict[key] = value
        
        with open('data/items_file.csv', mode='w') as file: # overwrite old file
            fieldnames = ['name', 'price', 'og_price', 'profit', 'shipping', 'platform_fee']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for value in result_dict.values():
                writer.writerow(value) # item dict 
        
        print(f'\nItem {search_term} deleted!\n')

    else:
        return

def search_item(key: str) -> Item:
    with open('data/items_file.csv', 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            if key in line:
                 key_item = Item(line[0], line[1], line[2], line[3], line[4])
                 print(f'\n{key_item}\n')
                 return key_item
            
        print('\nItem not Found!\n')
        return None
    
def edit_item(key: str):
    pass

def display_items():
    if os.path.isfile('data/items_file.csv'):
        print(f'\n{pd.read_csv('data/items_file.csv')}\n')
                
    else:
        print("FILE NOT FOUND.")

def get_net_prof_sum(): # list of net profits for all items
    # get items
    items = []
    with open('data/items_file.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            items.append(line)
    netprofits = []
    for item in items:
        # print(item)
        price = float(item["price"])
        cost = float(item["og_price"])
        shipping = float(item["shipping"])
        platform_fee = float(item["platform_fee"])
        # print(calc_net_prof(price, cost, shipping, platform_fee))
        netprofits.append(calc_net_prof(price, cost, shipping, platform_fee))
    
    net_prof_sum = calc_netprof_sum(netprofits)
    print(f'\nTotal net profit of all items: ${price:.2f}\n')

def get_price_sum():
    price = 0.0
    items = []
    with open('data/items_file.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            items.append(line)
    for item in items:
        price += float(item["og_price"])
    print(f'\nTotal amount spent: ${price:.2f}\n')