
def find_average(*args):
    print("Numbers received:", args)
    total = sum(args)
    avg = total / len(args) if args else 0
    return avg

print("=== Average Finder ===")
print("Enter numbers separated by space:")
nums = list(map(int, input().split()))

average = find_average(*nums)
print("Average of given numbers:", average)
