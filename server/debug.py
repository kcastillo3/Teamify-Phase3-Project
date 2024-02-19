import sys
import ipdb
from config import app
from models import *

def debug_database_operations():
    departments = Department.query.all()
    print(f"Departments: {departments}")
    employees = Employee.query.all()
    print(f"Employees: {employees}")

if __name__ == "__main__":
    with app.app_context():
        debug_database_operations()
        print("Entering interactive debugging session.")
        ipdb.set_trace()