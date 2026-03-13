from collections import defaultdict
from .addressbook import AddressBook


class AddressBookManager:
    def __init__(self):
        self.__address_books = dict()
        self.__city_to_persons = defaultdict(list)
        self.__state_to_persons = defaultdict(list)

    def add_addressbook(self, addressbook_name):
        if self.__address_books.__contains__(addressbook_name):
            raise ValueError("Address book already exists")
        self.__address_books[addressbook_name] = AddressBook(
            self._update_indecies, self._remove_from_indecies
        )

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

    def get_contacts_by_city(self):
        return self.__city_to_persons

    def get_contacts_by_state(self):
        return self.__state_to_persons

    def _update_indecies(self, contact):
        self.__city_to_persons[contact.city].append(contact)
        self.__state_to_persons[contact.state].append(contact)

    def _remove_from_indecies(self, contact):
        self.__city_to_persons[contact.city].remove(contact)
        self.__state_to_persons[contact.state].remove(contact)
