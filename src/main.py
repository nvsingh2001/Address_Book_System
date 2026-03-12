from models import Contact
from models import AddressBook
from utilities import main_menu, get_input

address_book = AddressBook()


def add_contact():
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


def main():
    while True:
        main_menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                add_contact()
            case "2":
                address_book.display_contacts()
                input("Press Enter to continue...")
            case "3":
                break


if __name__ == "__main__":
    main()
