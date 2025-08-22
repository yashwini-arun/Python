contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def get_contact(name):
    return contacts.get(name, "Not found")

def all_contacts():
    return contacts
