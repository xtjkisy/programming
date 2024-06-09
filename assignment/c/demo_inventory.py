from typing import Dict

class Inventory:
    def __init__(self) -> None:
        self.items: Dict[str, int] = {}

    def add_item(self, item_name: str, count: int) -> None:
        if item_name in self.items:
            self.items[item_name] += count
        else:
            self.items[item_name] = count

    def remove_item(self, item_name: str, count: int) -> None:
        if item_name in self.items:
            self.items[item_name] -= count
            if self.items[item_name] <= 0:
                del self.items[item_name]
        else:
            raise ValueError(f"Item '{item_name}' not found in inventory")

    def total_items(self) -> int:
        return sum(self.items.values())
