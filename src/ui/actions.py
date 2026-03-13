from models import Contact
from services.addressbook_manager import AddressBookManager
from ui.helper import get_input
from ui.menus import edit_contact_menu, search_contact_menu


def handle_add_addressbook(addressbook_services):
    try:
        addressbook_name = get_input("Address Book Name")
        addressbook_services.add_addressbook(addressbook_name)
        print(f"Address book '{addressbook_name}' created successfully.")
    except ValueError as e:
        print(f"Error creating address book: {e}")


def handle_view_contacts_by_location(
    addressbook_services: AddressBookManager, city=None, state=None
):
    try:
        if city:
            for city, contacts in addressbook_services.get_contacts_by_city().items():
                print(f"Contacts in {city}: \n".upper())
                for contact in contacts:
                    print(contact)
                print("#" * 50)
        elif state:
            for state, contacts in addressbook_services.get_contacts_by_state().items():
                print(f"Contacts in {state}: \n".upper())
                for contact in contacts:
                    print(contact)
                print("#" * 50)
    except Exception as e:
        print(f"Error during search: {e}")


def handle_open_addressbook(addressbook_services):
    try:
        addressbook_name = get_input("Address Book Name")
        address_book = addressbook_services.get_addressbook(addressbook_name)
        return address_book, addressbook_name
    except Exception as e:
        print(f"Error opening address book: {e}")
        return None, None


def handle_search_contacts(addressbook_manager: AddressBookManager):
    try:
        while True:
            search_contact_menu()
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    city = get_input("City")
                    display_search_results(
                        addressbook_manager.search_contacts(city=city)
                    )
                case "2":
                    state = get_input("State")
                    display_search_results(
                        addressbook_manager.search_contacts(state=state)
                    )
                case "3":
                    state = get_input("State")
                    city = get_input("City")
                    display_search_results(
                        addressbook_manager.search_contacts(city, state)
                    )
                case "4":
                    break
    except Exception as e:
        print(f"Error during search: {e}")


def display_search_results(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Total contacts found:", len(contacts))
        print("#" * 50)
        for contact in contacts:
            print(contact)
    input("\nPress Enter to continue...")


def handle_add_contact(address_book):
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
        print("Contact added successfully.")
    except Exception as e:
        print(f"Error adding contact: {e}")


def handle_edit_contact(address_book):
    try:
        name = input("Enter the full name of the contact (First Last): ").strip()
        parts = name.split()
        if len(parts) != 2:
            raise ValueError(
                "Invalid input. Please enter both First Name and Last Name."
            )

        first_name, last_name = parts
        contact = address_book.get_contact(first_name, last_name)
        if not contact:
            raise ValueError(f"Contact '{name}' not found.")

        edit_contact_menu()
        option = input("Enter your choice: ")

        match option:
            case "1":
                print(f"Current Number: {contact.phone_number}")
                contact.phone_number = get_input("New Phone Number")
            case "2":
                print(f"Current Email: {contact.email}")
                contact.email = get_input("New Email")
            case "3":
                print(f"Current Address: {contact.address}")
                contact.address = get_input("New Address")
            case "4":
                print(f"Current City: {contact.city}")
                contact.city = get_input("New City")
            case "5":
                print(f"Current State: {contact.state}")
                contact.state = get_input("New State")
            case "6":
                print(f"Current Zip Code: {contact.zip_code}")
                contact.zip_code = get_input("New Zip Code")
        print("Contact updated successfully.")
    except Exception as e:
        print(f"Error editing contact: {e}")


def handle_delete_contact(address_book):
    try:
        name = input("Enter the full name of the contact (First Last): ").strip()
        parts = name.split()
        if len(parts) != 2:
            raise ValueError(
                "Invalid input. Please enter both First Name and Last Name."
            )

        first_name, last_name = parts
        address_book.delete_contact(first_name, last_name)
        print("Contact deleted successfully")
    except Exception as e:
        print(f"Error deleting contact: {e}")


def handle_display_contacts(address_book):
    print("\n--- Contacts ---")
    print(address_book)
    input("\nPress Enter to continue...")


def handle_sort_contacts(address_book):
    address_book.sort_contacts()
    print("Contacts sorted successfully.")
    input("\nPress Enter to continue...")
