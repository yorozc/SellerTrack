from application import create_item, display_items, delete_item

def interface():
    print("Welcome to SellerTrack")
    option = input("What would you like to do: ")
    print("1. Create item\n" \
          "2. Display item\n" \
          "3. Delete item\n" \
          "4. Search for item\n")
    
    match option:
        case 1:
            item_name = input("Input name: ")
            item_price = input("Input price: ")
            item_og_price = input("Input original price: ")
            create_item(item_name, item_price, item_og_price)
        case 2:
            display_items()
        case 3:
            delete_item()
        case 4:
            pass

