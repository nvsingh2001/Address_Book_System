from utilities import get_input
from models import Contact
from utilities import edit_contact_menu


def add_contact(address_book):
    try:
        fields = [
            "First Name",
            "Last Name",
            "Phone Number",
            "Email",
            "Address",
            "City",
            "State",
            "Zip Code",
        ]

        values = [get_input(field) for field in fields]

        if address_book.get_contact(values[0], values[1]):
            raise ValueError("Contact already exists")

        address_book.add_contact(Contact(*values))

    except Exception as e:
        print(f"Error adding contact: {e}")


def edit_contact(address_book):
    try:
        name = input("Enter the full name of the contact: ")
        first_name, last_name = name.split(" ")
        contact = address_book.get_contact(first_name, last_name)
        if not contact:
            raise KeyError("Contact does not exists")

        edit_contact_menu()
        option = input("Enter your choice: ")

        match option:
            case "1":
                print(f"Contact Number: {contact.phone_number}")
                contact.phone_number = get_input("New Phone Number")
            case "2":
                print(f"Contact Email: {contact.email}")
                contact.email = get_input("New Phone Number")
            case "3":
                print(f"Contact Address: {contact.address}")
                contact.address = get_input("New Address")
            case "4":
                print(f"Contact City: {contact.city}")
                contact.city = get_input("New City")
            case "5":
                print(f"Contact State: {contact.state}")
                contact.state = get_input("New State")
            case "6":
                print(f"Contact Zip Code: {contact.zip_code}")
                contact.zip_code = get_input("New Zip Code")

    except Exception as e:
        print(f"Error while editing contact: {e}")


def delete_contact(address_book):
    try:
        name = input("Enter the full name of the contact: ")
        first_name, last_name = name.split(" ")
        contact = address_book.get_contact(first_name, last_name)
        if not contact:
            raise KeyError("Contact does not exists")

        address_book.delete_contact(contact)
        print("Contact deleted successfully")
    except Exception as e:
        print(f"Error while deleting contact: {e}")
