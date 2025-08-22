cart = []

def add_item(item, price):
    cart.append({"item": item, "price": price})

def total_amount():
    return sum(i["price"] for i in cart)

def show_cart():
    return [i["item"] for i in cart]
    