from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, contacts):
        pass


class SortByName(SortingStrategy):
    def sort(self, contacts):
        contacts.sort(
            key=lambda contact: (
                contact.first_name.casefold(),
                contact.last_name.casefold(),
            )
        )


class SortByCity(SortingStrategy):
    def sort(self, contacts):
        contacts.sort(key=lambda contact: contact.city.casefold())


class SortByState(SortingStrategy):
    def sort(self, contacts):
        contacts.sort(key=lambda contact: contact.state.casefold())


class SortByZipCode(SortingStrategy):
    def sort(self, contacts):
        contacts.sort(key=lambda contact: contact.zip_code.casefold())
