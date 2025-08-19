def add_book(library, title):
    library.append(title)
    return library

def remove_book(library, title):
    if title in library:
        library.remove(title)
        return f"{title} removed"
    return "Book not found"

def display_books(library):
    print("Books in library:")
    for book in library:
        print("-", book)

# Main program
library = ["Python 101", "Data Science", "AI Basics"]
display_books(library)

choice = input("Add or Remove book? ").lower()
title = input("Enter book name: ")

if choice == "add":
    add_book(library, title)
elif choice == "remove":
    print(remove_book(library, title))

display_books(library)
