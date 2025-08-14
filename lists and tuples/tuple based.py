coords = [(2,3),(5,6),(1,7),(4,4)]
for x,y in coords:
    distance = (x**2 + y**2)**0.5
    print(f"Point ({x},{y}) -> Distance: {distance:.2f}")
x_vals = [x for x,_ in coords]
y_vals = [y for _,y in coords]
print("X Values:", x_vals)
print("Y Values:", y_vals)
max_x = max(x_vals)
min_y = min(y_vals)
print("Max X:", max_x,"Min Y:",min_y)
