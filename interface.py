from application import create_item, display_items, delete_item, search_item, get_net_prof_sum, get_price_sum

def interface():
    print("Welcome to SellerTrack")
    print("1. Create item\n" \
          "2. Display item\n" \
          "3. Delete item\n" \
          "4. Search for item\n" \
          "5. Help\n" \
          "6. Get Total Price Sum\n"\
          "7. Get Total Profit\n"\
          "8. Exit")
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
            key = input("Insert Item to delete: ")
            delete_item(key)
        case 4:
            key = input("Item Name: ")
            search_item(key)
        case 5:
            pass
        case 6: # get total price sum
            # get input
            get_net_prof_sum()
        case 7: # get total profit
            get_price_sum()
        case 8:
            exit(0)
