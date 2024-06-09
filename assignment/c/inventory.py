from inventory import Inventory

def main() -> None:
    inventory = Inventory()
    
    # Add items
    inventory.add_item("apple", 10)
    inventory.add_item("banana", 20)
    inventory.add_item("apple", 5)
    print(f"Total items after adding: {inventory.total_items()}")  # Expected: 35

    # Remove items
    inventory.remove_item("banana", 5)
    print(f"Total items after removing 5 bananas: {inventory.total_items()}")  # Expected: 30

    # Remove all apples
    inventory.remove_item("apple", 15)
    print(f"Total items after removing all apples: {inventory.total_items()}")  # Expected: 15

    # Try to remove an item that doesn't exist
    try:
        inventory.remove_item("orange", 1)
    except ValueError as e:
        print(e)  # Expected: Item 'orange' not found in inventory

if __name__ == "__main__":
    main()
