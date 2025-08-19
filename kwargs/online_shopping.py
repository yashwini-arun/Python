

def shopping_cart(discount=0, **kwargs):
    print("=== Shopping Cart ===")
    total = sum(kwargs.values())
    print("Items Purchased:")
    for item, price in kwargs.items():
        print(f"{item}: ₹{price}")
    if discount > 0:
        total -= (total * discount) / 100
    print(f"Final Bill after {discount}% discount: ₹{total}")
    print("=" * 25)

# Main Program
shopping_cart(discount=10, Laptop=60000, Mouse=1200, Bag=1500)
shopping_cart(discount=5, Shoes=2500, Watch=3500)
