from abc import ABC, abstractmethod
from models.contact import Contact
import csv


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
        except IOError as e:
            print("Error saving file:", e)


class CsvFileIoStrategy(FileIoStrategy):
    def __init__(self):
        self.fieldnames = [
            "addressbook_name",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "address",
            "city",
            "state",
            "zip_code",
        ]

    def load_data(self, filename, addressbook_manager):
        try:
            with open(filename, mode="r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ab_name = row["address_book_name"]

                    if not addressbook_manager.exists(ab_name):
                        addressbook_manager.add_addressbook(ab_name)

                    new_contact = Contact(
                        row["first_name"],
                        row["last_name"],
                        row["phone_number"],
                        row["email"],
                        row["address"],
                        row["city"],
                        row["state"],
                        row["zip_code"],
                    )

                    addressbook_manager.get_addressbook(ab_name).add_contact(
                        new_contact
                    )
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error while loading the data", e)

    def save_data(self, filename, address_books):
        try:
            with open(filename, mode="w", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

                for ab_name, address_book in address_books.items():
                    for contact in address_book.get_contacts():
                        writer.writerow(
                            {
                                "addressbook_name": ab_name,
                                "first_name": contact.first_name,
                                "last_name": contact.last_name,
                                "phone_number": contact.phone_number,
                                "email": contact.email,
                                "address": contact.address,
                                "city": contact.city,
                                "state": contact.state,
                                "zip_code": contact.zip_code,
                            }
                        )
        except IOError as e:
            print("Error saving file:", e)
