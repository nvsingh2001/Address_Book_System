def get_input(field):
    while True:
        try:
            value = input(f"Enter {field}: ")
            if not value:
                raise ValueError(f"{field} cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            break
    return value
