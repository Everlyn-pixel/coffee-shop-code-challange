class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name  # Private attribute since it's immutable
        self._orders = []  # Private list to store orders
    
    @property
    def name(self):
        """Getter for coffee name (immutable once set)"""
        return self._name
    
    def orders(self):
        """Return all orders for this coffee"""
        return self._orders.copy()  # Return a copy to prevent external modification
    
    def customers(self):
        """Return unique list of customers who have ordered this coffee"""
        unique_customers = []
        for order in self._orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        """Return total count of orders for this coffee"""
        return len(self._orders)
    
    def average_price(self):
        """Return average price of all orders for this coffee"""
        if not self._orders:
            return 0
        
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
    
    def __repr__(self):
        return f"Coffee(name='{self.name}')"