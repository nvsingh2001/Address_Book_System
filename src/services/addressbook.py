class AddressBook:
    def __init__(self, on_add=None, on_delete=None):
        self.__contacts = list()
        self.__on_add_callback = on_add
        self.__on_delete_callback = on_delete

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
        if self.__on_add_callback:
            self.__on_add_callback(contact)

    def delete_contact(self, first_name, last_name):
        contact = self.get_contact(first_name, last_name)
        if not contact:
            raise KeyError("Contact does not exists")
        self.__contacts.remove(contact)
        if self.__on_delete_callback:
            self.__on_delete_callback(contact)

    def __str__(self):
        return "\n".join(str(contact) for contact in self.__contacts)

    def sort_contacts(self, strategy):
        strategy.sort(self.__contacts)
