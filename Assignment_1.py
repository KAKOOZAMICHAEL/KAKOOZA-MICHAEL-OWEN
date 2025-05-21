def add_item(inventory):
    """Add a new item to the inventory."""
    while True:
        print()
        name = input("Enter item name: ").strip()
        if not name:
            print()
            print("Error: Item name cannot be empty.")
            continue
        
        try:
            print()
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print()
                print("Error: Quantity cannot be negative.")
                continue
            print()
            price = float(input("Enter price per unit: "))
            if price < 0:
                print()
                print("Error: Price cannot be negative.")
                continue
        except ValueError:
            print()
            print("Error: Quantity and price must be valid numbers.")
            continue
        
        inventory.append({"name": name, "quantity": quantity, "price": price})
        print()
        print(f"Item '{name}' has been successfully stocked!")
        
        print()
        add_another = input("Do you want to add another item? (yes/no): ").strip().lower()
        if add_another != "yes":
            break

def update_item(inventory):
    """Update an existing item's quantity or price."""
    print()
    name = input("Enter item name to update: ").strip()
    if not name:
        print()
        print("Error: Item name cannot be empty.")
        return
    
    for item in inventory:
        if item["name"].lower() == name.lower():
            print()
            print(f"Item found! Current Quantity: {item['quantity']}")
            print()
            print(f"Current Price: Ugx.{item['price']:.2f}")
            try:
                print()
                new_quantity = input(f"Enter new quantity (or press Enter to keep {item['quantity']}): ").strip()
                if new_quantity:
                    print()
                    new_quantity = int(new_quantity)
                    if new_quantity < 0:
                        print()
                        print("Error: Quantity cannot be negative.")
                        return
                    item["quantity"] = new_quantity
                    print()                
                new_price = input(f"Enter new price (or press Enter to keep {item['price']}): ").strip()
                if new_price:
                    print()
                    new_price = float(new_price)
                    if new_price < 0:
                        print()
                        print("Error: Price cannot be negative.")
                        return
                    print()
                    item["price"] = new_price
                    print()
                
                print(f"Item '{name}' updated successfully!")
                return
            except ValueError:
                print()
                print("Error: Quantity and price must be valid numbers.")
                return
            print()
    
    print(f"Item '{name}' not found in inventory.")

def display_inventory(inventory):
    """Display all items in the inventory."""
    if not inventory:
        print()
        print("Inventory is empty.")
        return
    print()
    print("Current Inventory:")
    for index, item in enumerate(inventory, 1):
        print(f"Item {index}:")
        print(f"  Name: {item['name']}")
        print(f"  Quantity: {item['quantity']}")
        print(f"  Price: Ugx{item['price']:.2f}")
        print()

def remove_item(inventory):
    """Remove an item from the inventory."""
    print()
    name = input("Enter item name to remove: ").strip()
    if not name:
        print()
        print("Error: Item name cannot be empty.")
        return
    
    for i, item in enumerate(inventory):
        if item["name"].lower() == name.lower():
            inventory.pop(i)
            print()
            print(f"Item '{name}' removed successfully!")
            return
        print()
    
    print(f"Item '{name}' not found in inventory.")

def main():
    """Main function to run the inventory management system."""
    inventory = []
    
    while True:
        print()
        print("*---Inventory Management System---*")
        print()
        print("1. Add Item")
        print()
        print("2. Update Item")
        print()
        print("3. Display Inventory")
        print()
        print("4. Remove Item")
        print()
        print("5. Exit")
        print()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            print()
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print()
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()