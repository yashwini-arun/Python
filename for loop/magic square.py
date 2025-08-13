n = int(input("Enter size of square matrix: "))
matrix = []

print("Enter the matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

magic_sum = sum(matrix[0])
is_magic = True

for row in matrix:
    if sum(row) != magic_sum:
        is_magic = False

for col in range(n):
    if sum(matrix[row][col] for row in range(n)) != magic_sum:
        is_magic = False

if sum(matrix[i][i] for i in range(n)) != magic_sum:
    is_magic = False

if is_magic:
    print("It's a magic square!")
else:
    print("Not a magic square.")
