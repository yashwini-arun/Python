dna = "ATCGGATC"
complement = ""

for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "C":
        complement += "G"
    elif base == "G":
        complement += "C"

print("DNA:", dna)
print("Complement:", complement)
