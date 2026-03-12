class AddressBook:
    def __init__(self):
        self.__contacts = []

    def get_contact(self, first_name, last_name):
        for contact in self.__contacts:
            if (
                contact.first_name.casefold() == first_name.casefold()
                and contact.last_name.casefold() == last_name.casefold()
            ):
                return contact

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def display_contacts(self):
        for contact in self.__contacts:
            print("-" * 30)
            print(contact)
