message = "HELLO"
code = (3,1,4,5,2)
shuffled = ''.join([message[i-1] for i in code])
print("Original:", message)
print("Shuffled:", shuffled)
reversed_msg = shuffled[::-1]
print("Reversed Shuffled:", reversed_msg)
letters = tuple(shuffled)
print("Letters as tuple:", letters)
print("Joined again:", ''.join(letters))
