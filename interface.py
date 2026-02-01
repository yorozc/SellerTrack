from application import create_item, display_items, delete_item, search_item, get_net_prof_sum, get_price_sum, edit_item

def interface():
    print("Welcome to SellerTrack")
    print("1. Create item\n" \
          "2. Display item\n" \
          "3. Delete item\n" \
          "4. Edit item\n" \
          "5. Search for item\n" \
          "6. Help\n" \
          "7. Get Total Net Profit\n"\
          "8. Get Total Amount Spent\n"\
          "9. Exit")
    option = int(input("What would you like to do: "))
    match option:
        case 1:
            item_name = input("Input name: ")
            item_price = float(input("Input price: "))
            item_og_price = float(input("Input original price: "))
            shipping_fee = float(input("Input shipping fee: "))
            platform_fee = float(input("Input platform fee in percentage (%): "))
            create_item(item_name, item_price, item_og_price, shipping_fee, platform_fee)
        case 2:
            display_items()
        case 3:
            key = input("Insert Item to delete: ")
            delete_item(key)
        case 4:
            key = input("Insert Item to edit: ")
            edit_item(key)
        case 5: 
            key = input("Item Name: ")
            search_item(key)
        case 6: # help func
            pass
        case 7: # get net prof sum
            get_net_prof_sum()
        case 8: # get total price sum
            get_price_sum()
        case 9:
            exit(0)
