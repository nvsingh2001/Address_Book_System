class AddressBookManager:
    def __init__(self):
        self.__address_books = dict()

    def add_addressbook(self, addressbook_name, address_book):
        if self.__address_books.__contains__(addressbook_name):
            raise ValueError("Address book already exists")
        self.__address_books[addressbook_name] = address_book

    def __str__(self) -> str:
        return "\n".join(self.__address_books.keys())

    def get_addressbook(self, addressbook_name):
        return self.__address_books[addressbook_name]

    def delete_addressbook(self, addressbook_name):
        if not self.__address_books.__contains__(addressbook_name):
            raise ValueError("Address book does not exists")
        del self.__address_books[addressbook_name]

    def search_contacts(self, city=None, state=None):
        city = city.casefold() if city else None
        state = state.casefold() if state else None

        return [
            contact
            for addressbook in self.__address_books.values()
            for contact in addressbook.get_contacts()
            if (city is None or contact.city.casefold() == city)
            and (state is None or contact.state.casefold() == state)
        ]
