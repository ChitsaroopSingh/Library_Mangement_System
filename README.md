# Library Management System

A simple console-based Library Management System built with Python and MySQL. It lets you manage student records, book inventory, and book issue records through a menu-driven interface.

## Features

**View Data**
- List all student details
- List all book details
- List unavailable (issued out) books
- List available books

**Add Data**
- Register a new student
- Add a new book to the catalog
- Record a newly issued book

**Delete Data**
- Remove a student record
- Remove a book record

## Requirements

- Python 3.x
- MySQL Server (running locally)
- `mysql-connector-python` package

Install the required package:

```bash
pip install mysql-connector-python
```

## Setup

1. Make sure a MySQL server is running on your machine.
2. Open the script and replace the placeholder password:
   ```python
   con = sqltor.connect(host="localhost", user="root", password="ENTER YOUR MYSQL PASSWORD HERE")
   ```
3. Run the script:
   ```bash
   python library_management.py
   ```

On first run, the script automatically creates a `Library` database along with three tables: `Students`, `Books`, and `IssuedBooks`, if they don't already exist.

## Database Schema

**Students**
| Column | Type        | Notes       |
|--------|-------------|-------------|
| Addm   | int(5)      | Primary key |
| Name   | varchar(35) |             |
| Class  | varchar(3)  |             |

**Books**
| Column           | Type        | Notes       |
|------------------|-------------|-------------|
| BookCode         | int(5)      | Primary key |
| BookName         | varchar(35) |             |
| BookAvailability | varchar(3)  | "Yes"/"No"  |

**IssuedBooks**
| Column       | Type        | Notes       |
|--------------|-------------|-------------|
| BookCode     | int(5)      | Primary key |
| StudentName  | varchar(35) |             |
| BookName     | varchar(35) |             |

## Usage

Running the script displays a menu:

```
SHOW DATA FROM
1-Student Details
2-Book Details
3-Books Issued Details
4-Available Books

ADD DATA TO
5-Students
6-Books
7-Issued Books

DELETE DATA FROM
8-Students
9-Books
```

Enter the number corresponding to the action you want to perform, and follow the prompts.

## Known Issues

A few mismatches exist between the table schema and the queries, which will cause runtime errors if triggered:

- `add2()` inserts into columns `(Code, BookName, BookAvailability)`, but the `Books` table defines the column as `BookCode`, not `Code`.
- `dels2()` selects/deletes using `where code=...`, but again the actual column name is `BookCode`.
- Menu options 3 and 4 are swapped relative to their labels: choosing "3-Books Issued Details" calls `show3()` (unavailable books), and "4-Available Books" calls `show4()` (available books) — functionally fine, but there's no dedicated view for the `IssuedBooks` table itself.
- There's no input validation, so entering non-numeric text where an integer is expected (e.g., Admission Number, Book ID) will crash the program.
- No duplicate-key handling: attempting to add a student/book with an existing primary key will throw an unhandled MySQL error.

## Possible Improvements

- Fix the column name mismatches noted above.
- Add a dedicated function to view the `IssuedBooks` table.
- Wrap database calls in `try/except` blocks for graceful error handling.
- Add a "return book" feature that removes an entry from `IssuedBooks` and flips the book's availability back to "Yes".
- Loop the menu instead of exiting after a single action.
