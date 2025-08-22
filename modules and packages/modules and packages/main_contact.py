import contact_book

contact_book.add_contact("Alice", "9876543210")
contact_book.add_contact("Bob", "9123456780")

print("Alice's Number:", contact_book.get_contact("Alice"))
print("All Contacts:", contact_book.all_contacts())
