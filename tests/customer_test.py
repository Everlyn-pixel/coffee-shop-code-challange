import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clear the all_customers list before each test
        Customer.all_customers = []
        
    def test_customer_initialization(self):
        """Test Customer initialization with valid name"""
        customer = Customer("John")
        self.assertEqual(customer.name, "John")
    
    def test_customer_name_validation_string(self):
        """Test that customer name must be a string"""
        with self.assertRaises(TypeError):
            Customer(123)
    
    def test_customer_name_validation_length(self):
        """Test customer name length validation"""
        # Name too short
        with self.assertRaises(ValueError):
            Customer("")
        
        # Name too long
        with self.assertRaises(ValueError):
            Customer("ThisNameIsTooLongForValidation")
    
    def test_customer_name_setter(self):
        """Test customer name setter validation"""
        customer = Customer("John")
        
        # Valid name change
        customer.name = "Jane"
        self.assertEqual(customer.name, "Jane")
        
        # Invalid name change
        with self.assertRaises(ValueError):
            customer.name = ""
    
    def test_customer_orders_empty(self):
        """Test that new customer has no orders"""
        customer = Customer("John")
        self.assertEqual(len(customer.orders()), 0)
    
    def test_customer_coffees_empty(self):
        """Test that new customer has no coffees"""
        customer = Customer("John")
        self.assertEqual(len(customer.coffees()), 0)
    
    def test_customer_create_order(self):
        """Test creating an order through customer"""
        customer = Customer("John")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 3.50)
        
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 3.50)
        
        # Check that order is added to customer's orders
        self.assertEqual(len(customer.orders()), 1)
        self.assertIn(order, customer.orders())
    
    def test_customer_multiple_orders(self):
        """Test customer with multiple orders"""
        customer = Customer("John")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        
        order1 = customer.create_order(coffee1, 3.50)
        order2 = customer.create_order(coffee2, 4.25)
        
        self.assertEqual(len(customer.orders()), 2)
        self.assertEqual(len(customer.coffees()), 2)
        self.assertIn(coffee1, customer.coffees())
        self.assertIn(coffee2, customer.coffees())
    
    def test_customer_unique_coffees(self):
        """Test that customer.coffees() returns unique coffees"""
        customer = Customer("John")
        coffee = Coffee("Espresso")
        
        # Order same coffee twice
        order1 = customer.create_order(coffee, 3.50)
        order2 = customer.create_order(coffee, 3.75)
        
        self.assertEqual(len(customer.orders()), 2)
        self.assertEqual(len(customer.coffees()), 1)  # Should only have one unique coffee
    
    def test_most_aficionado_class_method(self):
        """Test the most_aficionado class method"""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        # Alice spends more on espresso
        customer1.create_order(coffee, 5.0)
        customer1.create_order(coffee, 4.0)  # Total: 9.0
        customer2.create_order(coffee, 3.0)  # Total: 3.0
        
        aficionado = Customer.most_aficionado(coffee)
        self.assertEqual(aficionado, customer1)
    
    def test_most_aficionado_no_orders(self):
        """Test most_aficionado returns None when no orders exist"""
        customer = Customer("John")
        coffee = Coffee("Espresso")
        
        result = Customer.most_aficionado(coffee)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()