import Item


def display_menu():
    print("\n--- GadgetGrove Inventory System ---")
    print("1. Add New Item")
    print("2. Change Item Name")
    print("3. Change Item Price")
    print("4. Restock Item")
    print("5. Find an Item")
    print("6. Print Inventory Summary")
    print("7. Exit")
    print("------------------------------------")


def main():
    inventory = {}

    while True:
        display_menu()
        choice = input("Please enter your choice (1-7): ")

        # ... (Choices 1, 2, 3 remain the same) ...
        if choice == '1':
            try:
                item_id = int(input("Enter new item ID: "))
                if item_id in inventory:
                    print("\nERROR: An item with this ID already exists.")
                    continue
                name = input("Enter item name: ")
                while True:
                    price = float(input("Enter item price: "))
                    if price >= 0: break
                    print("ERROR: Price cannot be negative.")
                while True:
                    quantity = int(input("Enter item quantity: "))
                    if quantity >= 0: break
                    print("ERROR: Quantity cannot be negative.")
                new_item = Item.Item(item_id, name, price, quantity)
                inventory[item_id] = new_item
                print(f"\nSUCCESS: '{name}' has been added to the inventory.")
            except ValueError:
                print("\nERROR: Invalid input.")
        elif choice == '2':
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                if item_id not in inventory:
                    print("\nERROR: Item ID not found.")
                else:
                    new_name = input("Enter the new name: ")
                    inventory[item_id].update_name(new_name)
            except ValueError:
                print("\nERROR: Please enter a valid number for the item ID.")
        elif choice == '3':
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                if item_id not in inventory:
                    print("\nERROR: Item ID not found.")
                else:
                    while True:
                        new_price = float(input("Enter the new price: "))
                        if new_price >= 0: break
                        print("ERROR: Price cannot be negative.")
                    inventory[item_id].update_price(new_price)
            except ValueError:
                print("\nERROR: Please enter a valid number for the ID or price.")

        # --- CHOICE 4: Restock Item (CORRECTED WITH VALIDATION) ---
        elif choice == '4':
            try:
                item_id = int(input("Enter the ID of the item to restock: "))
                if item_id in inventory:
                    # Input validation is now handled here, in the main loop.
                    while True:
                        quantity_to_add = int(
                            input(f"Enter the quantity to ADD to stock for '{inventory[item_id].name}': "))
                        if quantity_to_add > 0:
                            break
                        print("ERROR: Please enter a positive number to add.")

                    inventory[item_id].restock(quantity_to_add)
                else:
                    print("\nERROR: Item with that ID not found.")
            except ValueError:
                print("\nERROR: Please enter a valid number.")

        # ... (Choices 5, 6, 7 remain the same) ...
        elif choice == '5':
            query = input("Enter the ID or Name of the item to find: ")
            found_item = None
            try:
                item_id = int(query)
                if item_id in inventory:
                    found_item = inventory[item_id]
            except ValueError:
                for item in inventory.values():
                    if item.name.lower() == query.lower():
                        found_item = item
                        break
            if found_item:
                print("\n--- Item Found ---")
                print(found_item)
                print("--------------------")
            else:
                print("\nERROR: Item not found.")
        elif choice == '6':
            print("\n--- Current Inventory ---")
            if not inventory:
                print("The inventory is currently empty.")
            else:
                for item in inventory.values():
                    print(item)
            print("-------------------------")
        elif choice == '7':
            print("\nExiting the GadgetGrove Inventory System. Goodbye!")
            break
        else:
            print("\nERROR: Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()