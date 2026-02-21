from calc.calc_net_prof import calc_net_prof
from calc.calc_netprof_sum import calc_netprof_sum
from domain.item import Item #item object
import csv
import os
import pandas as pd

# TODO: add error handling

# helper func to just read csv file
def return_csv() -> list:
    items = []
    with open('items_file.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            items.append(line)
    return items

def overwrite_file(items: list):
    with open('items_file.csv', mode='w') as file: # overwrite old file
            fieldnames = ['name', 'price', 'og_price', 'profit', 'shipping', 'platform_fee']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for value in items:
                writer.writerow(value) # item dict 

def create_item(name: str, price: float, og_price: float, shipping_fee: float, platform_fee: float) -> Item:
    new_item = Item(name.lower(), price, og_price, shipping_fee, platform_fee)
    save_item(new_item)
    print("================\nItem Added!\n================\n")
    return new_item

def save_item(item: Item): # write to csv
    with open('items_file.csv', mode='a') as items_file:
        fieldnames = ['name', 'price', 'og_price', 'profit', 'shipping', 'platform_fee']
        writer = csv.DictWriter(items_file, fieldnames=fieldnames)
        if items_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'name': item.name, 'price': item.price, 'og_price':item.og_price, 'profit': item.price - item.og_price,
                         'shipping': item.shipping, 'platform_fee': item.platform_fee})
       
def delete_item(search_term: str):
    item = search_item(search_term)
    items = {}
    if item:
        result_dict = {}
        with open('items_file.csv', mode='r') as file: # read into items dict
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                items[f"{lines['name']}"] = lines

            # delete item by adding not found items to dictionary
            for key, value in items.items():
                if search_term != key:
                    result_dict[key] = value
        
        overwrite_file(result_dict) 
        
        print(f'\nItem {search_term} deleted!\n')

    else:
        return

def search_item(key: str) -> Item:
    with open('items_file.csv', 'r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            if key in line:
                 key_item = Item(line[0], line[1], line[2], line[3], line[4])
                 print(f'\n{key_item}\n')
                 return key_item
            
        print('\nItem not Found!\n')
        return None
    
def edit_item(key: str):
    items = return_csv()
    for item in items:
        if key == item["name"]:
            print("1. Edit Name\n"
                  "2. Edit Price\n"
                  "3. Edit Original Price\n"
                  "4. Edit Shipping\n"
                  "5. Edit Platform Fee\n") 
            option = int(input("What would you like to edit: "))
            match option:
                case 1:
                    new_name = input("Change item name: ")
                    item["name"] = new_name
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
            overwrite_file(items)
        else:
            print("Item not found")

    


def display_items():
    if os.path.isfile('items_file.csv'):
        print(pd.read_csv('items_file.csv'))
                
    else:
        print("FILE NOT FOUND.")

def get_net_prof_sum(): # list of net profits for all items
    # get items
    items = return_csv()

    netprofits = []
    for item in items:
        print(item)
        price = float(item["price"])
        cost = float(item["og_price"])
        shipping = float(item["shipping"])
        platform_fee = float(item["platform_fee"])
        print(calc_net_prof(price, cost, shipping, platform_fee))
        netprofits.append(calc_net_prof(price, cost, shipping, platform_fee))
    
    net_prof_sum = calc_netprof_sum(netprofits)
    print(f'\nTotal net profit of all items: ${net_prof_sum:.2f}\n')

def get_price_sum():
    price = 0.0
    items = return_csv()

    for item in items:
        price += float(item["og_price"])
    print(f'\nTotal amount spent: ${price:.2f}\n')