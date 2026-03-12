class AddressBook:
    def __init__(self):
        self.__contacts = list()

    def get_contact(self, first_name, last_name):
        for contact in self.__contacts:
            if (
                contact.first_name.casefold() == first_name.casefold()
                and contact.last_name.casefold() == last_name.casefold()
            ):
                return contact

    def add_contact(self, contact):
        if self.get_contact(contact.first_name, contact.last_name):
            raise ValueError("Contact already exists")
        self.__contacts.append(contact)

    def delete_contact(self, first_name, last_name):
        contact = self.get_contact(first_name, last_name)
        if not contact:
            raise KeyError("Contact does not exists")
        self.__contacts.remove(contact)

    def __str__(self):
        return "\n".join(str(contact) for contact in self.__contacts)
