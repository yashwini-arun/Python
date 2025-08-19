
def square_number(n):
    return n * n

print("=== Square Calculator ===")
print("Enter numbers separated by space:")
nums = list(map(int, input().split()))

squared = list(map(square_number, nums))

print("Original Numbers:", nums)
print("Squared Numbers :", squared)

for i in range(len(nums)):
    print(f"{nums[i]}^2 = {squared[i]}")
