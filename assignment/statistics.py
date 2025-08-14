# Mean, Median, Mode without libraries
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

# Mean
mean = sum(scores) / len(scores)

# Median
sorted_scores = sorted(scores)
n = len(sorted_scores)
median = (sorted_scores[n//2] if n % 2 != 0 
          else (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2)

# Mode
freq = {}
for num in scores:
    freq[num] = freq.get(num, 0) + 1
mode = max(freq, key=freq.get)

print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
