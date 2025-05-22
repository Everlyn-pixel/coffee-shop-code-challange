import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clear the all_customers list before each test
        Customer.all_customers = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")
    
    def test_order_initialization(self):
        """Test Order initialization with valid parameters"""
        order = Order(self.customer, self.coffee, 3.50)
        
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.50)
    
    def test_order_customer_validation(self):
        """Test that customer must be a Customer instance"""
        with self.assertRaises(TypeError):
            Order("not_a_customer", self.coffee, 3.50)
    
    def test_order_coffee_validation(self):
        """Test that coffee must be a Coffee instance"""
        with self.assertRaises(TypeError):
            Order(self.customer, "not_a_coffee", 3.50)
    
    def test_order_price_validation_type(self):
        """Test that price must be a number"""
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "not_a_price")
    
    def test_order_price_validation_range(self):
        """Test price range validation (1.0 - 10.0)"""
        # Price too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.50)
        
        # Price too high
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 15.0)
        
        # Valid prices at boundaries
        order1 = Order(self.customer, self.coffee, 1.0)
        order2 = Order(Customer("Bob"), self.coffee, 10.0)
        
        self.assertEqual(order1.price, 1.0)
        self.assertEqual(order2.price, 10.0)
    
    def test_order_price_accepts_int(self):
        """Test that price accepts integers and converts to float"""
        order = Order(self.customer, self.coffee, 5)  # int
        self.assertEqual(order.price, 5.0)
        self.assertIsInstance(order.price, float)
    
    def test_order_properties_immutable(self):
        """Test that order properties are immutable"""
        order = Order(self.customer, self.coffee, 3.50)
        
        # Should not be able to set customer
        with self.assertRaises(AttributeError):
            order.customer = Customer("Bob")
        
        # Should not be able to set coffee
        with self.assertRaises(AttributeError):
            order.coffee = Coffee("Latte")
        
        # Should not be able to set price
        with self.assertRaises(AttributeError):
            order.price = 5.0
    
    def test_order_relationships(self):
        """Test that order creates proper relationships"""
        order = Order(self.customer, self.coffee, 3.50)
        
        # Check that order is added to customer's orders
        self.assertIn(order, self.customer.orders())
        
        # Check that order is added to coffee's orders
        self.assertIn(order, self.coffee.orders())
        
        # Check that customer appears in coffee's customers
        self.assertIn(self.customer, self.coffee.customers())
        
        # Check that coffee appears in customer's coffees
        self.assertIn(self.coffee, self.customer.coffees())
    
    def test_order_repr(self):
        """Test order string representation"""
        order = Order(self.customer, self.coffee, 3.50)
        expected = "Order(customer=Alice, coffee=Espresso, price=3.5)"
        self.assertEqual(str(order), expected)
    
    def test_multiple_orders_same_customer_coffee(self):
        """Test multiple orders for same customer and coffee"""
        order1 = Order(self.customer, self.coffee, 3.50)
        order2 = Order(self.customer, self.coffee, 4.00)
        
        # Should have 2 orders
        self.assertEqual(len(self.customer.orders()), 2)
        self.assertEqual(len(self.coffee.orders()), 2)
        
        # But still only 1 unique customer and 1 unique coffee
        self.assertEqual(len(self.coffee.customers()), 1)
        self.assertEqual(len(self.customer.coffees()), 1)

if __name__ == '__main__':
    unittest.main()
