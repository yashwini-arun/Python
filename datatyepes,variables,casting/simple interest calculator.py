principal = 50000
rate = 5.0
time = 3
principal = float(principal)
rate = float(rate)
time = int(time)
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
print(f"The simple interest is: {simple_interest}")
print(f"The total amount after {rate}% interest over {time} year is : {total_amount}")