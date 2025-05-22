 # Debug script to test the coffee shop models
from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("🏪 Coffee Shop Challenge - Debug Script")
    print("=" * 50)
    
    # Create some customers
    print("\n📋 Creating Customers...")
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    print(f"Created: {alice}, {bob}, {charlie}")
    
    # Create some coffees
    print("\n☕ Creating Coffees...")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    print(f"Created: {espresso}, {latte}, {cappuccino}")
    
    # Create some orders
    print("\n🧾 Creating Orders...")
    order1 = alice.create_order(espresso, 3.50)
    order2 = bob.create_order(latte, 4.25)
    order3 = alice.create_order(latte, 4.50)
    order4 = charlie.create_order(espresso, 3.25)
    order5 = bob.create_order(espresso, 3.75)
    
    print(f"Created orders:")
    for order in [order1, order2, order3, order4, order5]:
        print(f"  - {order}")
    
    # Test customer methods
    print("\n👤 Testing Customer Methods...")
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    
    # Test coffee methods
    print("\n☕ Testing Coffee Methods...")
    print(f"Espresso orders: {espresso.num_orders()}")
    print(f"Espresso average price: ${espresso.average_price():.2f}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
    
    # Test the bonus method
    print("\n🏆 Testing Bonus Method...")
    aficionado = Customer.most_aficionado(espresso)
    if aficionado:
        print(f"Most espresso aficionado: {aficionado.name}")
    else:
        print("No espresso aficionado found")
    
    # Test validation
    print("\n⚠️  Testing Validation...")
    try:
        invalid_customer = Customer("")  # Should fail
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    try:
        invalid_coffee = Coffee("Hi")  # Should fail
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    try:
        invalid_order = Order(alice, espresso, 15.0)  # Should fail
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    main()
