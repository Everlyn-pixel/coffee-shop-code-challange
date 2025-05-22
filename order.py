class Order:
    def __init__(self, customer, coffee, price):
        # Validate and set customer
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        self._customer = customer
        
        # Validate and set coffee
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        self._coffee = coffee
        
        # Validate and set price
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(price)
        
        # Add this order to both customer and coffee order lists
        customer._orders.append(self)
        coffee._orders.append(self)
    
    @property
    def customer(self):
        """Getter for customer (immutable once set)"""
        return self._customer
    
    @property
    def coffee(self):
        """Getter for coffee (immutable once set)"""
        return self._coffee
    
    @property
    def price(self):
        """Getter for price (immutable once set)"""
        return self._price
    
    def __repr__(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"