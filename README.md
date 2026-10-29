# Employee Management System

A Python and MySQL project for managing employee records through basic CRUD operations.

## Project Status

A learning project demonstrating Python object-oriented programming and database connectivity.

## Features

- Retrieve all employee records.
- Add new employees.
- Retrieve an employee by ID.
- Update employee details.
- Delete employee records.

## Employee Information

The application works with employee fields including name, place, mobile number, email, department, salary, and joining date.

## Technologies Used

- Python
- MySQL
- `mysql-connector-python`
- `datetime`

## Concepts Practised

- Classes and inheritance
- MySQL database connectivity
- SQL CRUD operations
- Parameterized SQL queries
- Dynamic update queries
- Exception handling

## Setup

1. Install Python and MySQL.
2. Create a MySQL database named `company_db`.
3. Create the `employee` table with the columns used by the Python script.
4. Install the dependency:

```bash
pip install mysql-connector-python
```

5. Configure database credentials securely using environment variables.
6. Run the Python script.

## Future Improvements

- Add input validation.
- Improve error handling and database connection management.
- Prevent updates to unsupported column names.
- Add a user interface or REST API.
- Use environment variables for sensitive configuration.

## Note

This is a learning project and is not intended for production use without additional validation, security, and testing.
