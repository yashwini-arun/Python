list1 = [10,20,30]
list2 = [1,2,3]
merged = [val for pair in zip(list1,list2) for val in pair]
print("List1:", list1)
print("List2:", list2)
print("Merged Alternating:", merged)
squares = [x**2 for x in merged]
print("Squares:", squares)
even_nums = [x for x in merged if x%2==0]
print("Even Numbers:", even_nums)
sum_merged = sum(merged)
print("Sum of Merged:", sum_merged)
