# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items
# and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            # Assuming price is per unit
            total += quantity * price_dict[item]
        return total

# Dictionary to store prices of items
price_dict = {
    "Jaggery": 50,
    "Oil Pack": 104,
    "Tea": 40,
    "bread": 20,
    "milk": 25
}

# Example usage
cart = ShoppingCart()
cart.add_item("Jaggery", price_dict["Jaggery"], 2)
cart.add_item("Tea", price_dict["Tea"])
cart.add_item("bread", price_dict["bread"], 2)

print("Total Price : Rs.", cart.calculate_total())

cart.remove_item("bread")

print("Total Price after removing bread : Rs.", cart.calculate_total())
