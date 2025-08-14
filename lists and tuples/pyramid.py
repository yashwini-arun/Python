words = ["Python","AI","Data","ML"]
for word in words:
    stars = "*"*len(word)
    for i in range(1,len(word)+1):
        print(stars[:i])
    print("-"*len(word))
lengths = [len(w) for w in words]
print("Word lengths:", lengths)
print("Max length:", max(lengths))
print("Min length:", min(lengths))
print("Average length:", sum(lengths)/len(lengths))
