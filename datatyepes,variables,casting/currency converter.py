# Datatypes: float, str | Casting used
usd_str = input("enter the amount : ")  # amount in USD as string
usd = float(usd_str)
exchange_rate = 83.25  # INR per USD
inr = usd * exchange_rate

print(f"${usd} USD is equal to ₹{inr}")
