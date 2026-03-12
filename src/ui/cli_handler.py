from models import Contact
from services.addressbook_manager import AddressBookManager
from ui import (
    address_book_menu,
    get_input,
    edit_contact_menu,
)
from services import AddressBook
from ui.menus import search_contact_menu


def create_new_addressbook(addressbook_services):
    try:
        addressbook_name = get_input("Address Book Name")
        addressbook_services.add_addressbook(addressbook_name, AddressBook())
    except ValueError as e:
        print(f"Error creating address book: {e}")


def search_contacts(addressbook_manager: AddressBookManager):
    try:
        while True:
            search_contact_menu()
            options = input("Enter your choice: ")
            match options:
                case "1":
                    city = get_input("City")
                    contacts = addressbook_manager.search_contacts(city=city)
                    if not contacts:
                        print("No contacts found in this city.")
                    for contact in contacts:
                        print(contact)
                    input("Press enter to continue")
                case "2":
                    state = get_input("State")
                    contacts = addressbook_manager.search_contacts(state=state)
                    if not contacts:
                        print("No contacts found in this state.")
                    for contact in contacts:
                        print(contact)
                    input("Press enter to continue")
                case "3":
                    state = get_input("State")
                    city = get_input("City")
                    contacts = addressbook_manager.search_contacts(city, state)
                    if not contacts:
                        print("No contacts found in this city and state.")
                    for contact in contacts:
                        print(contact)
                    input("Press enter to continue")
                case "4":
                    break
    except Exception as e:
        print(f"Error: {e}")


def addressbook_menu(address_book):
    while True:
        address_book_menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                add_contact(address_book)
                input("Press Enter to continue...")
            case "2":
                print(address_book)
                input("Press Enter to continue...")
            case "3":
                edit_contact(address_book)
                input("Press Enter to continue...")
            case "4":
                delete_contact(address_book)
                input("Press Enter to continue...")
            case "5":
                break


def open_address_book(addressbook_services):
    try:
        addressbook_name = get_input("Address Book Name")
        address_book = addressbook_services.get_addressbook(addressbook_name)
        print(f"Opening address book: {addressbook_name}")
        addressbook_menu(address_book)
    except Exception as e:
        print(f"Error: {e}")


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

        address_book.add_contact(Contact(*values))

    except Exception as e:
        print(f"Error adding contact: {e}")


def edit_contact(address_book):
    try:
        name = input("Enter the full name of the contact: ")
        first_name, last_name = name.split(" ")
        contact = address_book.get_contact(first_name, last_name)

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
        address_book.delete_contact(first_name, last_name)
        print("Contact deleted successfully")
    except Exception as e:
        print(f"Error while deleting contact: {e}")
