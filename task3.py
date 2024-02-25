#Contact Management System

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name} has been deleted from contacts.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print(f"Contact {name} not found.")

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_manager.add_contact(contact)
        elif choice == '2':
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            contact_manager.display_all_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
