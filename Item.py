class Item:
    def __init__(self, item_id: int, name: str, price: float, quantity: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return (f"ID: {self.item_id}, Name: {self.name}, "
                f"Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_name(self, new_name: str):
        self.name = new_name
        print(f"\nSUCCESS: Item ID {self.item_id} name updated to '{self.name}'.")

    def update_price(self, new_price: float):
        self.price = new_price
        print(f"\nSUCCESS: Item ID {self.item_id} price updated to ${self.price:.2f}.")

    def restock(self, quantity_to_add: int):
        self.quantity += quantity_to_add
        print(f"\nSUCCESS: {quantity_to_add} units added. New stock for '{self.name}' is now {self.quantity}.")