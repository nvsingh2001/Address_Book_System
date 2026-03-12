class Contact:
    def __init__(
        self, first_name, last_name, phone_number, email, address, city, state, zip_code
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return (
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Email: {self.email}\n"
            f"Address: {self.address}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip Code: {self.zip_code}\n"
        )

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name
