
paragraph = """Python is a programming language. 
It is widely used for data science, web development, and automation. 
Python is simple and powerful."""

words = paragraph.lower().replace(",", "").replace(".", "").split()
print("Words in paragraph:", words)

unique_words = set(words)
print("\nUnique words in paragraph:", unique_words)

print("Total words:", len(words))
print("Unique word count:", len(unique_words))

repeated = [w for w in unique_words if words.count(w) > 1]
print("Repeated words:", repeated)
