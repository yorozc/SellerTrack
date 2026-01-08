from application import create_item, display_items, delete_item, search_item

def interface():
    print("Welcome to SellerTrack")
    print("1. Create item\n" \
          "2. Display item\n" \
          "3. Delete item\n" \
          "4. Search for item\n" \
          "5. Help\n" \
          "6. Exit")
    option = int(input("What would you like to do: "))
    match option:
        case 1:
            item_name = input("Input name: ")
            item_price = float(input("Input price: "))
            item_og_price = float(input("Input original price: "))
            create_item(item_name, item_price, item_og_price)
        case 2:
            display_items()
        case 3:
            delete_item()
        case 4:
            search_item()
        case 5:
            pass
        case 6:
            exit(0)
