from services.file_io import JsonFileIoStrategy
from ui import (
    main_menu,
    create_new_addressbook,
    open_address_book,
    search_contacts,
)
from services import AddressBookManager
from ui.cli_handler import view_contacts_by_location

CSV_FILENAME = "address_book.csv"
TEXT_FILENAME = "address_book.txt"
JSON_FILENAME = "address_book.json"


def main():
    addressbook_services = AddressBookManager(JsonFileIoStrategy())
    addressbook_services.load_data(JSON_FILENAME)
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
                addressbook_services.save_data(JSON_FILENAME)
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
