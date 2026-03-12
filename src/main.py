from models import AddressBook
from utilities import main_menu, add_contact, edit_contact

address_book = AddressBook()


def main():
    while True:
        main_menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                add_contact(address_book)
                input("Press Enter to continue...")
            case "2":
                address_book.display_contacts()
                input("Press Enter to continue...")
            case "3":
                edit_contact(address_book)
                input("Press Enter to continue...")
            case "4":
                break


if __name__ == "__main__":
    main()
