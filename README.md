# Address Book System

A flexible and extensible contact management application built with Python. This system demonstrates clean architecture principles, specifically focusing on the Open/Closed Principle (OCP) through the use of design patterns like Strategy and Dependency Injection.

## Features

- **Multiple Address Books**: Create and manage multiple independent address books.
- **Contact Management**: Add, update, and delete contacts with detailed information (Name, Phone, Email, Address, City, State, Zip).
- **Global Search**: Search for contacts by City or State across all managed address books.
- **Location-Based Grouping**: View contacts grouped by their City or State for better organization.
- **Advanced Sorting**: Sort contacts within an address book by Name, City, State, or Zip Code.
- **Flexible Persistence**: Support for multiple file formats (JSON, CSV, Text) to save and load data.

## Architecture

The project is designed with extensibility in mind, adhering to modern software engineering standards:

- **Open/Closed Principle (OCP)**: The system can be extended with new persistence or sorting methods without modifying existing core logic.
- **Strategy Pattern**: Used for both persistence (`FileIoStrategy`) and sorting (`SortingStrategy`), allowing interchangeable algorithms at runtime.
- **Dependency Injection**: The `AddressBookManager` is injected with a persistence strategy, making it decoupled from specific file formats.

## Persistence Strategies

The system currently supports the following I/O strategies:
- `JsonFileIoStrategy`: Saves data in a structured JSON format (Default).
- `CsvFileIoStrategy`: Exports and imports data using standard CSV files.
- `TextFileIoStrategy`: Uses a custom pipe-separated (`|`) text format.

## Sorting Strategies

Contacts can be sorted using:
- `SortByName`: Sorts alphabetically by first name, then last name.
- `SortByCity`: Sorts alphabetically by city.
- `SortByState`: Sorts alphabetically by state.
- `SortByZipCode`: Sorts numerically/alphabetically by ZIP code.

## Directory Structure

```text
.
├── src/
│   ├── main.py              # Application entry point
│   ├── models/
│   │   └── contact.py       # Contact data model
│   ├── services/
│   │   ├── addressbook.py   # Core AddressBook logic
│   │   ├── addressbook_manager.py # Management of multiple books
│   │   ├── file_io.py       # Persistence strategies
│   │   └── sorting.py       # Sorting strategies
│   └── ui/
│       ├── actions.py       # UI action handlers
│       ├── cli_handler.py   # CLI-specific display logic
│       ├── helper.py        # UI utilities
│       └── menus.py         # Menu definitions
├── address_book.json        # Data files (examples)
├── address_book.csv
└── address_book.txt
```

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Running the Application

Navigate to the project root and run:

```bash
python src/main.py
```

### Usage

Follow the on-screen menu to:
1. Create a new address book.
2. Open an existing address book to manage contacts.
3. List all available address books.
4. Search contacts globally by location.
5. View grouped contact summaries.
6. Save and exit.
