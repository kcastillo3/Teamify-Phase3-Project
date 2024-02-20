from config import app, migrate
from models import db, Department, Employee

def get_all_departments():
    return Department.query.all()

def display_all_departments():
    departments = get_all_departments()
    if departments:
        print(f"{'ID':<4} | {'Department Name':<20}")
        print("-" * 26)  

        for department in departments:
            print(f"{department.id:<4} | {department.name:20}")
    else:
        print("No departments found.")
    print()

def find_department_by_id(department_id):
    try:
        department_id = int(department_id)
    except ValueError:
        print("Please enter a valid number for the department ID.")
        return None
    department = db.session.get(Department, department_id)
    if department is None:
        print(f"No department found with id {department_id}")
    return department

def choose_department_by_id():
    department_id = input("Enter department id: ")
    department = find_department_by_id(department_id)
    if department:
        print(f"\nId: {department.id}, Name: {department.name}\n")
    press_enter_to_continue()

def show_departments_employees():
    display_all_departments()
    department_id = input("Enter department id: ")
    department = find_department_by_id(department_id)
    if department:
        if department.employees:
            header = f"{'ID':<4} | {'Name':<20} | {'Position':<25} | {'Email':<30} | {'Availability':<15} | {'Department':<20}"
            print(header)
            print("-" * len(header))
            for employee in department.employees:
                print(f"{employee.id:<4} | {employee.name:20} | {employee.position:25} | {employee.email:30} | {employee.availability:15} | {department.name:20}")
        else:
            print("No employees in this department.")
    press_enter_to_continue()

def add_department():
    department_name = input("Enter department name: ")
    existing_department = Department.query.filter_by(name=department_name).first()
    if existing_department:
        print("Department with this name already exists.")
    else:
        new_department = Department(name=department_name)
        try:
            db.session.add(new_department)
            db.session.commit()
            print(f"Added department {department_name}")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding department: {e}")
    press_enter_to_continue()

def delete_department():
    display_all_departments()
    department_id = input("Enter department id: ")
    department = find_department_by_id(department_id)
    if department:
        confirmation = input(f"Are you sure you want to delete department with id {department_id}? (yes/no): ")
        if confirmation.lower() == 'yes':
            if department.employees:
                print("This department has employees. Please choose a department to move them to.")
                display_all_departments()
                new_department_id = input("Enter new department id: ")
                new_department = find_department_by_id(new_department_id)
                if new_department and new_department.id != department.id:
                    for employee in department.employees:
                        employee.department_id = new_department.id
                    db.session.commit()  
                    try:
                        db.session.delete(department)
                        db.session.commit()
                        print(f"Deleted department with id {department_id}")
                    except Exception as e:
                        db.session.rollback()
                        print(f"Error deleting department: {e}")
                else:
                    print("Invalid department id. Operation cancelled.")
            else:
                try:
                    db.session.delete(department)
                    db.session.commit()
                    print(f"Deleted department with id {department_id}")
                except Exception as e:
                    db.session.rollback()
                    print(f"Error deleting department: {e}")
        else:
            print("Operation cancelled.")
    press_enter_to_continue()

def find_employee_by_id(employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Please enter a valid number for the employee ID.")
        return None
    employee = db.session.get(Employee, employee_id)
    if employee is None:
        print(f"No employee found with id {employee_id}")
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
            print(f"Moved {employee.name} from {old_department.name if old_department else 'No department'} to {new_department.name}")
        except Exception as e:
            db.session.rollback()
            print(f"Error moving employee to department: {e}")
    else:
        print("Employee not found.")

def add_employee():
    display_all_departments()
    department_id = input("Enter the ID of the department to add a new employee to: ")
    department = find_department_by_id(department_id)
    if department:
        employee_name = input("Enter employee name: ")
        employee_position = input("Enter employee position: ")
        employee_email = input("Enter employee email: ")
        employee_availability = input("Enter employee availability: ") 
        employee = Employee(name=employee_name, position=employee_position, email=employee_email, availability=employee_availability, department_id=department.id)
        try:
            db.session.add(employee)
            db.session.commit()
            print(f"Added {employee.name} to {department.name}")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding employee to department: {e}")
    else:
        print("Department not found.")
    press_enter_to_continue()

def display_all_employees():
    employees = Employee.query.all()
    if employees:
        header = f"{'ID':<4} | {'Name':<20} | {'Position':<25} | {'Email':<30} | {'Availability':<15} | {'Department':<20}"
        print(header)
        print("-" * len(header))

        for employee in employees:
            department = db.session.get(Department, employee.department_id)
            department_name = department.name if department else 'No department'
            print(f"{employee.id:<4} | {employee.name:20} | {employee.position:25} | {employee.email:30} | {employee.availability:15} | {department_name:20}")
    else:
        print("No employees found.")
    print()


def delete_employee():
    display_all_employees()
    employee_id = input("Enter employee id: ")
    employee = find_employee_by_id(employee_id)
    if employee:
        confirmation = input(f"Are you sure you want to delete employee with id {employee_id}? (yes/no): ")
        if confirmation.lower() == 'yes':
            try:
                db.session.delete(employee)
                db.session.commit()
                print(f"Deleted employee with id {employee_id}")
            except Exception as e:
                db.session.rollback()
                print(f"Error deleting employee: {e}")
        else:
            print("Operation cancelled.")
    press_enter_to_continue()

def update_employee():
    employee_id = input("Enter employee id: ")
    employee = find_employee_by_id(employee_id)
    if employee:
        new_name = input("Enter new name (leave blank to keep current): ")
        new_position = input("Enter new position (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        new_availability = input("Enter new availability (leave blank to keep current): ")
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
            print(f"Updated employee with id {employee_id}")
        except Exception as e:
            db.session.rollback()
            print(f"Error updating employee: {e}")
    press_enter_to_continue()

def press_enter_to_continue():
    input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
  with app.app_context():
      migrate.init_app(app, db)
      db.create_all()
      while True:
          print("\nTeamify\n")
          print("1. Manage Departments")
          print("2. Manage Employees")
          print("3. Exit\n")
          choice = input("Enter your choice: ")
          if choice == '1':
            while True:
                print("\nManage Departments\n")
                display_all_departments()
                print("\n1. Add Department")
                print("2. Delete Department")
                print("3. Show Department's Employees")
                print("4. Move Employee to Department")
                print("5. Back to Main Menu")
                choice = input("\nEnter your choice: ")
                if choice == '1':
                    add_department()
                elif choice == '2':
                    delete_department()
                elif choice == '3':
                    show_departments_employees()
                elif choice == '4':
                    display_all_departments()
                    display_all_employees()
                    print("Choose the department to move the employee to:")
                    department_id = input("Enter department ID: ")
                    department = find_department_by_id(department_id)
                    if department:
                        employee_id = input("Enter employee ID to move: ")
                        add_employee_to_department(department, employee_id)
                    else:
                        print("Invalid department ID.")
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
          elif choice == '2':
              while True:
                  print("\nManage Employees\n")
                  display_all_employees()  
                  print("1. Add Employee")
                  print("2. Delete Employee")
                  print("3. Update Employee")
                  print("4. Back to Main Menu\n")
                  sub_choice = input("Enter your choice: ")
                  if sub_choice == '1':
                      add_employee()
                  elif sub_choice == '2':
                      delete_employee()
                  elif sub_choice == '3':
                      update_employee()
                  elif sub_choice == '4':
                      break
                  else:
                      print("Invalid choice. Please choose again.")
          elif choice == '3':
              break
