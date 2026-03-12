class AddressBook:
    def __init__(self):
        self.__contacts = list()

    def get_contacts(self):
        return self.__contacts

    def get_contact(self, first_name, last_name):
        for contact in self.__contacts:
            if (
                contact.first_name.casefold() == first_name.casefold()
                and contact.last_name.casefold() == last_name.casefold()
            ):
                return contact
        return None

    def add_contact(self, contact):
        if contact in self.__contacts:
            raise ValueError("Contact already exists")
        self.__contacts.append(contact)

    def delete_contact(self, first_name, last_name):
        contact = self.get_contact(first_name, last_name)
        if not contact:
            raise KeyError("Contact does not exists")
        self.__contacts.remove(contact)

    def __str__(self):
        return "\n".join(str(contact) for contact in self.__contacts)
