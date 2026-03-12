class AddressBookManager:
    def __init__(self):
        self.__address_book = dict()

    def add_addressbook(self, addressbook_name, address_book):
        if self.__address_book.__contains__(addressbook_name):
            raise ValueError("Address book already exists")
        self.__address_book[addressbook_name] = address_book

    def __str__(self) -> str:
        return "\n".join(self.__address_book.keys())

    def get_addressbook(self, addressbook_name):
        return self.__address_book[addressbook_name]

    def delete_addressbook(self, addressbook_name):
        if not self.__address_book.__contains__(addressbook_name):
            raise ValueError("Address book does not exists")
        del self.__address_book[addressbook_name]
