import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clear the all_customers list before each test
        Customer.all_customers = []
    
    def test_coffee_initialization(self):
        """Test Coffee initialization with valid name"""
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")
    
    def test_coffee_name_validation_string(self):
        """Test that coffee name must be a string"""
        with self.assertRaises(TypeError):
            Coffee(123)
    
    def test_coffee_name_validation_length(self):
        """Test coffee name minimum length validation"""
        # Name too short
        with self.assertRaises(ValueError):
            Coffee("Hi")
        
        # Valid minimum length
        coffee = Coffee("Tea")
        self.assertEqual(coffee.name, "Tea")
    
    def test_coffee_name_immutable(self):
        """Test that coffee name is immutable (no setter)"""
        coffee = Coffee("Espresso")
        
        # Should not be able to set name directly
        with self.assertRaises(AttributeError):
            coffee.name = "Latte"
    
    def test_coffee_orders_empty(self):
        """Test that new coffee has no orders"""
        coffee = Coffee("Espresso")
        self.assertEqual(len(coffee.orders()), 0)
    
    def test_coffee_customers_empty(self):
        """Test that new coffee has no customers"""
        coffee = Coffee("Espresso")
        self.assertEqual(len(coffee.customers()), 0)
    
    def test_coffee_num_orders_empty(self):
        """Test num_orders returns 0 for new coffee"""
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.num_orders(), 0)
    
    def test_coffee_average_price_empty(self):
        """Test average_price returns 0 for coffee with no orders"""
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.average_price(), 0)
    
    def test_coffee_with_orders(self):
        """Test coffee with orders"""
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        order1 = Order(customer1, coffee, 3.50)
        order2 = Order(customer2, coffee, 4.50)
        
        # Test orders
        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(len(coffee.orders()), 2)
        self.assertIn(order1, coffee.orders())
        self.assertIn(order2, coffee.orders())
        
        # Test customers
        self.assertEqual(len(coffee.customers()), 2)
        self.assertIn(customer1, coffee.customers())
        self.assertIn(customer2, coffee.customers())
        
        # Test average price
        expected_average = (3.50 + 4.50) / 2
        self.assertEqual(coffee.average_price(), expected_average)
    
    def test_coffee_unique_customers(self):
        """Test that coffee.customers() returns unique customers"""
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        
        # Same customer orders twice
        order1 = Order(customer, coffee, 3.50)
        order2 = Order(customer, coffee, 4.50)
        
        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(len(coffee.customers()), 1)  # Should only have one unique customer
        self.assertIn(customer, coffee.customers())
    
    def test_coffee_average_price_calculation(self):
        """Test average price calculation with multiple orders"""
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        
        expected_average = (2.0 + 4.0 + 6.0) / 3
        self.assertEqual(coffee.average_price(), expected_average)

if __name__ == '__main__':
    unittest.main()
