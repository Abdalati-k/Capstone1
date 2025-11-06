
from Item import Item
from HighEndElectronic import HighEndElectronic
from BrandedClothing import BrandedClothing

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

        if choice == '1':
            try:
                print("\n--- Add a New Item ---")
                print("1. Standard Item")
                print("2. High-End Electronic (with Warranty)")
                print("3. Branded Clothing (with Size/Color)")
                item_type = input("What type of item would you like to add? (1-3): ")

                if item_type not in ['1', '2', '3']:
                    print("\nERROR: Invalid item type.")
                    continue

                item_id = int(input("Enter new item ID: "))
                if item_id in inventory:
                    print("\nERROR: An item with this ID already exists.")
                    continue

                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))

                new_item = None
                if item_type == '1':
                    new_item = Item(item_id, name, price, quantity)
                elif item_type == '2':
                    warranty = int(input("Enter warranty period (in months): "))
                    new_item = HighEndElectronic(item_id, name, price, quantity, warranty)
                elif item_type == '3':
                    size = input("Enter item size (e.g., S, M, L, XL): ")
                    color = input("Enter item color: ")
                    new_item = BrandedClothing(item_id, name, price, quantity, size, color)

                inventory[item_id] = new_item
                print(f"\nSUCCESS: '{name}' has been added to the inventory.")

            except ValueError:
                print("\nERROR: Invalid input. Please enter the correct data types.")

        # --- OTHER CHOICES (NO CHANGES NEEDED!) ---

        elif choice == '2':  # Change Name
            # This works for any item type because they all inherit 'update_name'
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                if item_id not in inventory:
                    print("\nERROR: Item ID not found.")
                else:
                    new_name = input("Enter the new name: ")
                    inventory[item_id].update_name(new_name)
            except ValueError:
                print("\nERROR: Please enter a valid number for the item ID.")

        elif choice == '3':  # Change Price
            # This works for any item type because they all inherit 'update_price'
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                if item_id not in inventory:
                    print("\nERROR: Item ID not found.")
                else:
                    new_price = float(input("Enter the new price: "))
                    inventory[item_id].update_price(new_price)
            except ValueError:
                print("\nERROR: Please enter a valid number.")

        elif choice == '4':  # Restock
            # This works for any item type because they all inherit 'restock'
            try:
                item_id = int(input("Enter the ID of the item to restock: "))
                if item_id in inventory:
                    quantity_to_add = int(input(f"Enter quantity to ADD for '{inventory[item_id].name}': "))
                    inventory[item_id].restock(quantity_to_add)
                else:
                    print("\nERROR: Item with that ID not found.")
            except ValueError:
                print("\nERROR: Please enter a valid number.")

        elif choice == '5':  # Find Item
            # This works for any item type
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
                print(found_item)  # Polymorphism in action!
                print("--------------------")
            else:
                print("\nERROR: Item not found.")

        elif choice == '6':  # Print Summary
            print("\n--- Current Inventory ---")
            if not inventory:
                print("The inventory is currently empty.")
            else:
                for item in inventory.values():
                    # POLYMORPHISM: Python automatically calls the correct __str__
                    # for each object, whether it's an Item, Electronic, or Clothing.
                    print(item)
            print("-------------------------")

        elif choice == '7':
            print("\nExiting the GadgetGrove Inventory System. Goodbye!")
            break
        else:
            print("\nERROR: Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()