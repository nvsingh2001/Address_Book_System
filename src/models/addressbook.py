class AddressBook:
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def display_contacts(self):
        for contact in self.__contacts:
            print("-" * 30)
            print(contact)
