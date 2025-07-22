# inventory.py - Simple Inventory Management System
class InventorySystem:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {
                'quantity': quantity,
                'price': price
            }
        return True
    
    def remove_item(self, name, quantity):
        if name not in self.items:
            return False
        
        if self.items[name]['quantity'] < quantity:
            return False
        
        self.items[name]['quantity'] -= quantity
        if self.items[name]['quantity'] == 0:
            del self.items[name]
        return True
    
    def get_item_info(self, name):
        return self.items.get(name, None)
    
    def get_total_value(self):
        total = 0
        for item in self.items.values():
            total += item['quantity'] * item['price']
        return total
    
    def get_low_stock_items(self, threshold=5):
        low_stock = []
        for name, info in self.items.items():
            if info['quantity'] <= threshold:
                low_stock.append(name)
        return low_stock
    
    def list_all_items(self):
        return list(self.items.keys())

# Example usage
if __name__ == "__main__":
    inventory = InventorySystem()
    
    # Add items
    inventory.add_item("Laptop", 10, 999.99)
    inventory.add_item("Mouse", 25, 29.99)
    inventory.add_item("Keyboard", 3, 79.99)
    
    # Check inventory
    print(f"Total inventory value: ${inventory.get_total_value():.2f}")
    print(f"Low stock items: {inventory.get_low_stock_items()}")
    
    # Remove some items
    inventory.remove_item("Mouse", 20)
    print(f"After sale - Mouse info: {inventory.get_item_info('Mouse')}")
