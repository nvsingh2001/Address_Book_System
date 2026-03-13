from services.file_io import TextFileIoStrategy
from ui import (
    main_menu,
    create_new_addressbook,
    open_address_book,
    search_contacts,
)
from services import AddressBookManager
from ui.cli_handler import view_contacts_by_location

FILENAME = "address_book.txt"

# For test
# addressbook_services = AddressBookManager()
#
# addressbook_services.add_addressbook("default")
#
# address_book = addressbook_services.get_addressbook("default")
#
# contacts = [
#     Contact(
#         f"First{i}",
#         f"Last{i}",
#         f"900000{str(i).zfill(4)}",
#         f"user{i}@example.com",
#         f"{100 + i} Example Street",
#         ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"][i % 5],
#         ["NY", "CA", "IL", "TX", "AZ"][i % 5],
#         f"{10000 + i}",
#     )
#     for i in range(1, 201)
# ]
#
# random.shuffle(contacts)
#
#
# for contact in contacts:
#     address_book.add_contact(contact)


def main():
    addressbook_services = AddressBookManager()
    addressbook_services.load_data(FILENAME, TextFileIoStrategy())
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
                view_contacts_by_location(addressbook_services)
            case "6":
                addressbook_services.save_data(FILENAME, TextFileIoStrategy())
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
