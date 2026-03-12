from models import AddressBook, Contact
from utilities import main_menu, add_contact, edit_contact, delete_contact

address_book = AddressBook()

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
                add_contact(address_book)
                input("Press Enter to continue...")
            case "2":
                address_book.display_contacts()
                input("Press Enter to continue...")
            case "3":
                edit_contact(address_book)
                input("Press Enter to continue...")
            case "4":
                delete_contact(address_book)
                input("Press Enter to continue...")
            case "5":
                break


if __name__ == "__main__":
    main()
