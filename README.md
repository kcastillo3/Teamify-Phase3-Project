# Teamify

# Project Overview:
Teamify is a command-line interface (CLI) based application, designed to streamline the management of employee records and departmental assignments for small to medium-sized retail managers. This tool simplifies administrative tasks, making it easier to manage a dynamic retail environment efficiently.

# Owner:
Kevin

# Domain Model:
Employee -----< Department

Employee: Contains basic information such as name and contact details, and is linked to a department.

Department: Represents different departments within the store, each having multiple employees.

# User Stories:

View all employees: List every employee in the system, with options to filter by department.

Add new employees: Input basic employee information and assign them to a department.

Update employee records: Edit details of existing employee records, including changing their department.

Delete employees: Remove employee records from the system when necessary.

Manage departments: Create new departments, update existing ones, and delete departments, ensuring that employee associations are maintained accurately.

# To Begin:

1. Clone the repository to your local machine using `git clone <repository_url>`.
2. Navigate to the project directory with `cd <project_directory>`.
3. Install Pipenv, a tool for managing dependencies and virtual environments, with `pip install pipenv`.
4. Install the necessary dependencies with `pipenv install`.
5. Activate the Pipenv shell with `pipenv shell`.
6. Set up the database by running `python server/seed.py`.
7. Start the application with `python server/app.py`.