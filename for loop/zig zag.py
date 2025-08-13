rows = 3
cols = 15
for i in range(rows):
    for j in range(cols):
        if ((i + j) % 4 == 0) or (i == 1 and j % 2 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
