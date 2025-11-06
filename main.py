
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
                print("2. High-End Electronic")
                print("3. Branded Clothing ")
                item_type = input("What type of item would you like to add? (1-3): ")

                if item_type not in ['1', '2', '3']:
                    print("\nERROR: Invalid item type.")
                    continue

                item_id = int(input("Enter new item ID: "))
                if item_id in inventory:
                    print("\nERROR: An item with this ID already exists.")
                    continue

                name = input("Enter item name: ")


                while True:
                    try:
                        price_str = input("Enter item price: ")
                        price = float(price_str)
                        if price >= 0:
                            break
                        else:
                            print("ERROR: Price cannot be negative. Please try again.")
                    except ValueError:
                        print("ERROR: Invalid input. Please enter a valid number for the price.")

                while True:
                    try:
                        quantity_str = input("Enter item quantity: ")
                        quantity = int(quantity_str)
                        if quantity >= 0:
                            break
                        else:
                            print("ERROR: Quantity cannot be negative. Please try again.")
                    except ValueError:
                        print("ERROR: Invalid input. Please enter a valid whole number for the quantity.")


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
                    new_price = float(input("Enter the new price: "))
                    if new_price >= 0:
                        inventory[item_id].update_price(new_price)
                    else:
                        print("\nERROR: Price cannot be negative.")
            except ValueError:
                print("\nERROR: Please enter a valid number.")

        elif choice == '4':
            try:
                item_id = int(input("Enter the ID of the item to restock: "))
                if item_id in inventory:
                    # And you could add validation for restock quantity here
                    quantity_to_add = int(input(f"Enter quantity to ADD for '{inventory[item_id].name}': "))
                    if quantity_to_add >= 0:
                         inventory[item_id].restock(quantity_to_add)
                    else:
                        print("\nERROR: Quantity to add cannot be negative.")
                else:
                    print("\nERROR: Item with that ID not found.")
            except ValueError:
                print("\nERROR: Please enter a valid number.")

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