class ShoppingCart:
    def __init__(self):
        # Dictionary to store items with name as key and price as value
        self.items = {}

    def add_item(self, name, price):
        """
        Adds an item to the cart.

        Parameters:
        - name (str): Name of the item
        - price (float or int): Price of the item

        Raises:
        - TypeError: If name is not a string or price is not a number
        - ValueError: If price is negative
        """
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Item price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.items[name] = price

    def remove_item(self, name):
        """
        Removes an item from the cart by name.

        Parameters:
        - name (str): Name of the item to be removed
        """
        if name in self.items:
            del self.items[name]

    def total_price(self):
        """
        Returns the total price of all items in the cart.

        Returns:
        - float: Sum of item prices
        """
        return sum(self.items.values())

    def list_items(self):
        """
        Returns all items in the cart as a dictionary.

        Returns:
        - dict: Items with name as key and price as value
        """
        return self.items


# -------------------------------------
# 🔽 Sample usage with test data
# -------------------------------------

if __name__ == "__main__":
    cart = ShoppingCart()

    # Sample items
    sample_items = {
        "Apple": 30,
        "Bread": 25.5,
        "Milk": 42.75,
        "Eggs": 60,
        "Coffee": 150
    }

    # Add sample items to the cart
    for name, price in sample_items.items():
        cart.add_item(name, price)

    # Remove an item
    cart.remove_item("Eggs")

    # Print all items
    print("🛒 Items in Cart:")
    for name, price in cart.list_items().items():
        print(f"- {name}: ₹{price}")

    # Print total
    print(f"\n💰 Total Price: ₹{cart.total_price():.2f}")
