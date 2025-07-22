"""
inventory.py - Simple Inventory Management System

FUNCTIONALITY OVERVIEW:
This module implements a basic InventorySystem class for tracking product inventory with:
- Adding items to inventory (with quantity and price)
- Removing items from inventory with stock validation
- Retrieving item information and availability
- Calculating total inventory value
- Identifying low-stock items that need reordering
- Basic inventory reporting and listing


WHAT TO REVIEW:
- Functionality and logic
- Data structure choices and efficiency
- Input validation and error handling
- Code organization and naming conventions

"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple

class InventorySystem:
    """
    A comprehensive inventory management system that tracks items,
    quantities, prices, and transaction history.
    """
    
    def __init__(self):
        self.items: Dict[str, Dict] = {}
        self.transaction_history: List[Dict] = []
    
    def add_item(self, name: str, quantity: int, price: float) -> bool:
        """
        Add items to inventory or update existing item quantity.
        
        Args:
            name: Item name
            quantity: Number of items to add
            price: Price per unit
            
        Returns:
            True if successful
        """
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {
                'quantity': quantity,
                'price': price,
                'last_updated': datetime.now().isoformat()
            }
        
        self._log_transaction('ADD', name, quantity, price)
        return True
    
    def remove_item(self, name: str, quantity: int) -> bool:
        """
        Remove items from inventory.
        
        Args:
            name: Item name  
            quantity: Number of items to remove
            
        Returns:
            True if successful, False if insufficient stock
        """
        if name not in self.items:
            return False
        
        if self.items[name]['quantity'] < quantity:
            return False
        
        price = self.items[name]['price']
        self.items[name]['quantity'] -= quantity
        self.items[name]['last_updated'] = datetime.now().isoformat()
        
        if self.items[name]['quantity'] == 0:
            del self.items[name]
            
        self._log_transaction('REMOVE', name, quantity, price)
        return True
    
    def get_item_info(self, name: str) -> Optional[Dict]:
        """Get detailed information about a specific item."""
        return self.items.get(name, None)
    
    def get_total_value(self) -> float:
        """Calculate total monetary value of all inventory."""
        total = 0
        for item in self.items.values():
            total += item['quantity'] * item['price']
        return total
    
    def get_low_stock_items(self, threshold: int = 5) -> List[str]:
        """Get list of items with stock below threshold."""
        low_stock = []
        for name, info in self.items.items():
            if info['quantity'] <= threshold:
                low_stock.append(name)
        return low_stock
    
    def list_all_items(self) -> List[str]:
        """Get list of all item names in inventory."""
        return list(self.items.keys())
    
    def _log_transaction(self, transaction_type: str, item_name: str, 
                        quantity: int, price: float) -> None:
        """
        Private method to log all inventory transactions.
        
        Args:
            transaction_type: 'ADD' or 'REMOVE'
            item_name: Name of the item
            quantity: Quantity involved in transaction  
            price: Price per unit
        """
        self.transaction_history.append({
            'type': transaction_type,
            'item': item_name,
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now().isoformat(),
            'total_value': quantity * price
        })
    
    def get_transaction_history(self, item_name: Optional[str] = None) -> List[Dict]:
        """
        Get transaction history, optionally filtered by item name.
        
        Args:
            item_name: Optional item name to filter by
            
        Returns:
            List of transaction records
        """
        if item_name:
            return [t for t in self.transaction_history if t['item'] == item_name]
        return self.transaction_history.copy()
    
    def generate_inventory_report(self) -> Dict[str, any]:
        """
        Generate comprehensive inventory report.
        
        Returns:
            Dictionary containing inventory statistics and summaries
        """
        total_items = len(self.items)
        total_value = self.get_total_value()
        low_stock = self.get_low_stock_items()
        
        return {
            'total_unique_items': total_items,
            'total_inventory_value': total_value,
            'low_stock_items': low_stock,
            'low_stock_count': len(low_stock),
            'report_generated_at': datetime.now().isoformat()
        }

# Example usage
if __name__ == "__main__":
    inventory = InventorySystem()
    
    # Add items
    inventory.add_item("Laptop", 10, 999.99)
    inventory.add_item("Mouse", 25, 29.99)
    inventory.add_item("Keyboard", 3, 79.99)
    
    # Generate report
    report = inventory.generate_inventory_report()
    print(f"Inventory Report:")
    print(f"  Total Items: {report['total_unique_items']}")
    print(f"  Total Value: ${report['total_inventory_value']:.2f}")
    print(f"  Low Stock: {report['low_stock_items']}")
