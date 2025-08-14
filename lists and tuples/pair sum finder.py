nums = [2,4,6,8,3]
target = 10
pairs = [(x,y) for i,x in enumerate(nums) for j,y in enumerate(nums) if i<j and x+y==target]
print("Numbers:", nums)
print("Pairs summing to", target, ":", pairs)
sum_pairs = [x+y for x,y in pairs]
print("Sum of each pair:", sum_pairs)
tuple_pairs = tuple(pairs)
print("Pairs as tuple:", tuple_pairs)
flat = [num for p in pairs for num in p]
print("Flattened list of pairs:", flat)
