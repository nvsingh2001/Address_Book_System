from models import Contact
from ui import (
    main_menu,
    create_new_addressbook,
    open_address_book,
)
from services import AddressBookManager, AddressBook
from ui.cli_handler import search_contacts

# For test
addressbook_services = AddressBookManager()

addressbook_services.add_addressbook("default", AddressBook())

address_book = addressbook_services.get_addressbook("default")

address_book.add_contact(
    Contact(
        "John",
        "Doe",
        "1234567890",
        "p4g0e@example.com",
        "123 Main St",
        "Anytown",
        "CA",
        "12345",
    )
)


def main():
    while True:
        main_menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                create_new_addressbook(addressbook_services)
                input("Press Enter to continue...")
            case "2":
                open_address_book(addressbook_services)
            case "3":
                print("List of Address Books:")
                print(addressbook_services)
                input("Press Enter to continue...")
            case "4":
                search_contacts(addressbook_services)
            case "5":
                break


if __name__ == "__main__":
    main()
