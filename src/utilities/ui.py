import os

banner = r"""


/$$$$$$        /$$       /$$                                              /$$$$$$$                      /$$      
/$$__  $$      | $$      | $$                                             | $$__  $$                    | $$      
| $$  \ $$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$
| $$$$$$$$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____//$$_____/      | $$$$$$$  /$$__  $$ /$$__  $$| $$  /$$/
| $$__  $$| $$  | $$| $$  | $$| $$  \__/| $$$$$$$$|  $$$$$$|  $$$$$$       | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/ 
| $$  | $$| $$  | $$| $$  | $$| $$      | $$_____/ \____  $$\____  $$      | $$  \ $$| $$  | $$| $$  | $$| $$_  $$ 
| $$  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
|__/  |__/ \_______/ \_______/|__/       \_______/|_______/|_______/       |_______/  \______/  \______/ |__/  \__/
                                                                                                                
                                                                                                                
                                                                                                                    """


def main_menu():
    welcome_screen()
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")


def edit_contact_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    print("Edit Contact Menu")
    print("-----------------")
    print("1. Edit Phone number")
    print("2. Edit Email")
    print("3. Edit Address")
    print("4. Edit City")
    print("5. Edit State")
    print("6. Edit Zip Code")


def welcome_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    print("WELCOME TO YOUR ADDRESS BOOK")
    print("----------------------------")
