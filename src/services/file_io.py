from abc import ABC, abstractmethod
from models.contact import Contact


class FileIoStrategy(ABC):
    @abstractmethod
    def load_data(self, filename, addressbook_manager):
        pass

    @abstractmethod
    def save_data(self, filename, address_books):
        pass


class TextFileIoStrategy(FileIoStrategy):
    def load_data(self, filename, addressbook_manager):
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split("|")

                    if len(parts) == 9:
                        (
                            ab_name,
                            first_name,
                            last_name,
                            phone_number,
                            email,
                            address,
                            city,
                            state,
                            zip_code,
                        ) = parts

                        if not addressbook_manager.exists(ab_name):
                            addressbook_manager.add_addressbook(ab_name)

                        new_contact = Contact(
                            first_name,
                            last_name,
                            phone_number,
                            email,
                            address,
                            city,
                            state,
                            zip_code,
                        )
                        addressbook_manager.get_addressbook(ab_name).add_contact(
                            new_contact
                        )
            print("File loaded successfully")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"An error occured while loading: {e}")

    def save_data(self, filename, address_books):
        try:
            with open(filename, mode="w", encoding="utf-8") as file:
                for ab_name, address_book in address_books.items():
                    for contact in address_book.get_contacts():
                        line = f"{ab_name}|{contact.first_name}|{contact.last_name}|{contact.phone_number}|{contact.email}|{contact.address}|{contact.city}|{contact.state}|{contact.zip_code}\n"
                        file.write(line)
            print("File saved successfully")
        except IOError as e:
            print("Error saving file:", e)
