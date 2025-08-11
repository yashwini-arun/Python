
movie = input("Enter the movie name: ")
ticket_price_str = "250"
tickets_str = input("Enter the number of tickets:")

ticket_price = float(ticket_price_str)
tickets = int(tickets_str)
total_cost = ticket_price * tickets

print(f"Movie: {movie}")
print(f"Tickets: {tickets}")
print(f"Total Cost: ₹{total_cost}")
