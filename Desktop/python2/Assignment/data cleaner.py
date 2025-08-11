number_str = "0123"

print("Original string:", number_str)
print("Type before cleaning:", type(number_str))

cleaned_number_str = number_str.lstrip("0") or "0"

number_int = int(cleaned_number_str)

print("Cleaned number:", number_int)
print("Type after cleaning:", type(number_int))
