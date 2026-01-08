from application import create_item

def interface():
    print("Welcome to SellerTrack")
    item_name = input("Input name: ")
    item_price = input("Input price: ")
    item_og_price = input("Input original price: ")
    item = create_item(item_name, item_price, item_og_price)
    print(item)

