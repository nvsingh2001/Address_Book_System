from ui.menus import address_book_menu, view_contact_menu
from ui import actions


def create_new_addressbook(addressbook_services):
    actions.handle_add_addressbook(addressbook_services)


def view_contacts_by_location(addressbook_services):
    while True:
        view_contact_menu()
        option = input("Enter your choice: ")

        match option:
            case "1":
                actions.handle_view_contacts_by_location(
                    addressbook_services, city=True
                )
                input("Press Enter to continue...")
            case "2":
                actions.handle_view_contacts_by_location(
                    addressbook_services, state=True
                )
                input("Press Enter to continue...")
            case "3":
                break


def open_address_book(addressbook_services):
    address_book, name = actions.handle_open_addressbook(addressbook_services)
    if address_book:
        print(f"Opening address book: {name}")
        manage_addressbook(address_book)


def search_contacts(addressbook_manager):
    actions.handle_search_contacts(addressbook_manager)


def manage_addressbook(address_book):
    while True:
        address_book_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                actions.handle_add_contact(address_book)
            case "2":
                actions.handle_display_contacts(address_book)
            case "3":
                actions.handle_edit_contact(address_book)
            case "4":
                actions.handle_delete_contact(address_book)
            case "5":
                break


def add_contact(address_book):
    actions.handle_add_contact(address_book)


def edit_contact(address_book):
    actions.handle_edit_contact(address_book)


def delete_contact(address_book):
    actions.handle_delete_contact(address_book)
