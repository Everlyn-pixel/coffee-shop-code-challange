class Customer:
    # Class variable to keep track of all customers for the bonus method
    all_customers = []
    
    def __init__(self, name):
        self.name = name  # This will use the setter for validation
        Customer.all_customers.append(self)
        self._orders = []  # Private list to store orders
    
    @property
    def name(self):
        """Getter for customer name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for customer name with validation"""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    
    def orders(self):
        """Return all orders for this customer"""
        return self._orders.copy()  # Return a copy to prevent external modification
    
    def coffees(self):
        """Return unique list of coffees this customer has ordered"""
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        """Create a new order for this customer"""
        from order import Order  # Import here to avoid circular imports
        new_order = Order(self, coffee, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        """Return the customer who has spent the most on the given coffee"""
        customer_totals = {}
        
        # Calculate total spent by each customer on this coffee
        for customer in cls.all_customers:
            total_spent = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total_spent += order.price
            if total_spent > 0:
                customer_totals[customer] = total_spent
        
        # Return customer with highest total, or None if no orders
        if not customer_totals:
            return None
        
        return max(customer_totals, key=customer_totals.get)
    
    def __repr__(self):
        return f"Customer(name='{self.name}')"