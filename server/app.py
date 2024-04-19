from art import *
from config import app, migrate
from models import db, Department, Employee
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from art import text2art
from rich.style import Style
from rich.text import Text
import time

console = Console()

def get_all_departments():
    return Department.query.all()

def display_all_departments():
    departments = get_all_departments()
    if departments:
        table = Table(title="Departments", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Department Name", min_width=20)
        for department in departments:
            table.add_row(str(department.id), department.name)
        console.print(table)
    else:
        console.print("No departments found.", style="bold red")

def find_department_by_id(department_id):
    try:
        department_id = int(department_id)
    except ValueError:
        console.print("Please enter a valid number for the department ID.", style="bold red")
        return None
    department = db.session.get(Department, department_id)
    if not department:
        console.print(f"No department found with id {department_id}", style="bold red")
    return department

def show_departments_employees():
    display_all_departments()
    department_id = console.input("Enter department id: ")
    department = find_department_by_id(department_id)
    if department and department.employees:
        table = Table(title=f"Employees in {department.name}", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", min_width=20)
        table.add_column("Position")
        table.add_column("Email")
        table.add_column("Availability")
        table.add_column("Department")
        for employee in department.employees:
            table.add_row(str(employee.id), employee.name, employee.position, employee.email, employee.availability, department.name)
        console.print(table)
    else:
        console.print("No employees in this department.", style="bold red")
    press_enter_to_continue()

def add_department():
    department_name = console.input("Enter department name: ")
    existing_department = Department.query.filter_by(name=department_name).first()
    if existing_department:
        console.print("Department with this name already exists.", style="bold red")
    else:
        new_department = Department(name=department_name)
        try:
            db.session.add(new_department)
            db.session.commit()
            console.print(f"Added department {department_name}", style="bold green")
        except Exception as e:
            db.session.rollback()
            console.print(f"Error adding department: {e}", style="bold red")
    press_enter_to_continue()

def delete_department():
    display_all_departments()
    department_id = console.input("Enter department id: ")
    department = find_department_by_id(department_id)
    if department:
        confirmation = console.input(f"Are you sure you want to delete department with id {department_id}? (yes/no): ")
        if confirmation.lower() == 'yes':
            if department.employees:
                console.print("This department has employees. Please choose a department to move them to.", style="bold red")
                display_all_departments()
                new_department_id = console.input("Enter new department id: ")
                new_department = find_department_by_id(new_department_id)
                if new_department and new_department.id != department.id:
                    for employee in department.employees:
                        employee.department_id = new_department.id
                    db.session.commit()
                    try:
                        db.session.delete(department)
                        db.session.commit()
                        console.print(f"Deleted department with id {department_id}", style="bold green")
                    except Exception as e:
                        db.session.rollback()
                        console.print(f"Error deleting department: {e}", style="bold red")
                else:
                    console.print("Invalid department id. Operation cancelled.", style="bold red")
            else:
                try:
                    db.session.delete(department)
                    db.session.commit()
                    console.print(f"Deleted department with id {department_id}", style="bold green")
                except Exception as e:
                    db.session.rollback()
                    console.print(f"Error deleting department: {e}", style="bold red")
        else:
            console.print("Operation cancelled.", style="bold yellow")
    press_enter_to_continue()

def find_employee_by_id(employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        console.print("Please enter a valid number for the employee ID.", style="bold red")
        return None
    employee = db.session.get(Employee, employee_id)
    if not employee:
        console.print(f"No employee found with id {employee_id}", style="bold red")
    return employee

def add_employee_to_department(department, employee_id):
    department_id = department.id
    employee_id = int(employee_id)
    employee = db.session.get(Employee, employee_id)
    if employee:
        old_department_id = employee.department_id
        employee.department_id = department_id
        try:
            db.session.commit()
            old_department = db.session.get(Department, old_department_id) if old_department_id else None
            new_department = db.session.get(Department, department_id)
            console.print(f"Moved {employee.name} from {old_department.name if old_department else 'No department'} to {new_department.name}", style="bold green")
        except Exception as e:
            db.session.rollback()
            console.print(f"Error moving employee to department: {e}", style="bold red")
    else:
        console.print("Employee not found.", style="bold red")

def add_employee():
    display_all_departments()
    department_id = console.input("Enter the ID of the department to add a new employee to: ")
    department = find_department_by_id(department_id)
    if department:
        employee_name = console.input("Enter employee name: ")
        employee_position = console.input("Enter employee position: ")
        employee_email = console.input("Enter employee email: ")
        employee_availability = console.input("Enter employee availability: ")
        employee = Employee(name=employee_name, position=employee_position, email=employee_email, availability=employee_availability, department_id=department.id)
        try:
            db.session.add(employee)
            db.session.commit()
            console.print(f"Added {employee.name} to {department.name}", style="bold green")
        except Exception as e:
            db.session.rollback()
            console.print(f"Error adding employee to department: {e}", style="bold red")
    else:
        console.print("Department not found.", style="bold red")
    press_enter_to_continue()

def display_all_employees():
    employees = Employee.query.all()
    if employees:
        table = Table(title="All Employees", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", min_width=20)
        table.add_column("Position")
        table.add_column("Email")
        table.add_column("Availability")
        table.add_column("Department")
        for employee in employees:
            department = db.session.get(Department, employee.department_id)
            department_name = department.name if department else 'No department'
            table.add_row(str(employee.id), employee.name, employee.position, employee.email, employee.availability, department_name)
        console.print(table)
    else:
        console.print("No employees found.", style="bold red")
    press_enter_to_continue()

def delete_employee():
    display_all_employees()
    employee_id = console.input("Enter employee id: ")
    employee = find_employee_by_id(employee_id)
    if employee:
        confirmation = console.input(f"Are you sure you want to delete employee with id {employee_id}? (yes/no): ")
        if confirmation.lower() == 'yes':
            try:
                db.session.delete(employee)
                db.session.commit()
                console.print(f"Deleted employee with id {employee_id}", style="bold green")
            except Exception as e:
                db.session.rollback()
                console.print(f"Error deleting employee: {e}", style="bold red")
        else:
            console.print("Operation cancelled.", style="bold yellow")
    press_enter_to_continue()

def update_employee():
    employee_id = console.input("Enter employee id: ")
    employee = find_employee_by_id(employee_id)
    if employee:
        new_name = console.input("Enter new name (leave blank to keep current): ")
        new_position = console.input("Enter new position (leave blank to keep current): ")
        new_email = console.input("Enter new email (leave blank to keep current): ")
        new_availability = console.input("Enter new availability (leave blank to keep current): ")
        if new_name:
            employee.name = new_name
        if new_position:
            employee.position = new_position
        if new_email:
            employee.email = new_email
        if new_availability:
            employee.availability = new_availability
        try:
            db.session.commit()
            console.print(f"Updated employee with id {employee_id}", style="bold green")
        except Exception as e:
            db.session.rollback()
            console.print(f"Error updating employee: {e}", style="bold red")
    press_enter_to_continue()

def press_enter_to_continue():
    console.input("\nPress Enter to return to the main menu...")

# Generate ASCII art using 'art' with the "isometric1" font
teamify_art = text2art("Teamify", font="isometric1")

# Define the color scheme with bold blue text on a black background
tron_style = Style(color="blue", bgcolor="black", bold=True)

# Print the ASCII art with the chosen style
console.print(teamify_art, style=tron_style)

# Simple animation: blinking text

console.print(Panel("[bold blue]Welcome to Teamify![/bold blue]", style="bold cyan on black"), style="bold blue")

def tron_theme_menu():
    # Simplified menu presentation
    menu_options = ["1. Manage Departments", "2. Manage Employees", "3. Exit"]
    for option in menu_options:
        console.print(f"[bold cyan]{option}[/bold cyan]", style="bold cyan on black")
    choice = Prompt.ask("[bold magenta]Enter your choice[/bold magenta]", choices=["1", "2", "3"], default="1")
    return choice

if __name__ == "__main__":
    with app.app_context():
        migrate.init_app(app, db)
        db.create_all()
        while True:
            choice = tron_theme_menu()
            if choice == '1':
                while True:
                    rprint("\n[bold cyan]Manage Departments[/bold cyan]\n")
                    display_all_departments()
                    console.print("1. Add Department", style="magenta on black")
                    console.print("2. Delete Department", style="magenta on black")
                    console.print("3. Show Department's Employees", style="magenta on black")
                    console.print("4. Move Employee to Department", style="magenta on black")
                    console.print("5. Back to Main Menu", style="magenta on black")
                    choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5"], default="1")
                    if choice == '1':
                        add_department()
                    elif choice == '2':
                        delete_department()
                    elif choice == '3':
                        show_departments_employees()
                    elif choice == '4':
                        display_all_departments()
                        display_all_employees()
                        console.print("Choose the department to move the employee to:", style="bold blue on black")
                        department_id = Prompt.ask("Enter department ID")
                        department = find_department_by_id(department_id)
                        if department:
                            employee_id = Prompt.ask("Enter employee ID to move")
                            add_employee_to_department(department, employee_id)
                        else:
                            console.print("Invalid department ID.", style="bold red on black")
                    elif choice == '5':
                        break
                    else:
                        console.print("Invalid choice. Please try again.", style="bold red on black")
            elif choice == '2':
                while True:
                    rprint("\n[bold cyan]Manage Employees[/bold cyan]\n")
                    display_all_employees()
                    console.print("1. Add Employee", style="magenta on black")
                    console.print("2. Delete Employee", style="magenta on black")
                    console.print("3. Update Employee", style="magenta on black")
                    console.print("4. Back to Main Menu\n", style="magenta on black")
                    sub_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"], default="1")
                    if sub_choice == '1':
                        add_employee()
                    elif sub_choice == '2':
                        delete_employee()
                    elif sub_choice == '3':
                        update_employee()
                    elif sub_choice == '4':
                        break
                    else:
                        console.print("Invalid choice. Please choose again.", style="bold red on black")
            elif choice == '3':
                console.print("[bold red]Exiting...[/bold red]", style="bold red on black")
                break