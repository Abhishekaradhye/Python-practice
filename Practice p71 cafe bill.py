print('----------------- Welcome to Green Forest Cafe -----------------')

menu = {
    'Cold Coffee': 80, 'Coffee': 25, 'Tea': 20, 
    'Cheese Pizza': 90, 'Special Veges Pizza': 120, 
    'Cheese Burger': 80, 'King Burger': 100, 
    'Roasted Sandwich': 70, 'Grilled Sandwich': 80,
    'French Fries': 80, 'Fried Rice': 70,
    'Veg Manchurian': 110, 'Paneer Manchurian': 130
}

def take_order():
    print("\nHello foodie, what would you like to have today :) !\n")
    for item, price in menu.items():
        print(f"{item.ljust(25)}: Rs. {price}")

    order_input = input('\nEnter your order (e.g., 2 coffee, 1 fried rice): ').split(',')

    bill_total = 0
    print("\n----- Order Summary -----")
    for entry in order_input:
        parts = entry.strip().split(' ', 1)
        if len(parts) == 2 and parts[0].isdigit():
            quantity = int(parts[0])
            item_name = parts[1].strip().title()
            if item_name in menu:
                item_total = quantity * menu[item_name]
                print(f"Order Taken as {quantity} x {item_name} @ Rs.{menu[item_name]} = Rs.{item_total}   :)")
                bill_total += item_total
            else:
                print(item, 'is not available in our cafe :) !')
        else:
            print(f"Invalid entry: '{entry.strip()}' :(")

    print(f"\nDear Foodie, Your Total Bill is Rs. {bill_total}")

take_order()
