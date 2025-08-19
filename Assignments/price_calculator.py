

def add_gst(price):
    gst_rate = 0.18  # 18% GST
    return round(price + (price * gst_rate), 2)

print("=== Price Calculator with GST ===")
prices = list(map(float, input("Enter product prices (space separated): ").split()))

final_prices = list(map(add_gst, prices))

print("\nBill Details:")
for p, f in zip(prices, final_prices):
    print(f"Original: ₹{p:.2f}  -->  With GST: ₹{f:.2f}")

print("\nTotal Bill Amount: ₹", sum(final_prices))
