from config import db, app
from models import Department, Employee

def seed_departments():
    departments = [
        {"name": "Sales Floor"},
        {"name": "Stock Room"},
        {"name": "Security"}
    ]

    for dept in departments:
        existing_department = Department.query.filter_by(name=dept["name"]).first()
        if not existing_department:
            Department.create(name=dept["name"])

def seed_employees():
    employees = [
        {"name": "Jubin Luke", "address": "123 Main St", "email": "jb@gmail.com", "position": "Store Manager", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Megan Black", "address": "456 Maple Ave", "email": "meganb@yahoo.com", "position": "Assistant Store Manager", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Caleb O'Leary", "address": "789 Oak Dr", "email": "olearycaleb@protonmail.com", "position": "Assistant Store Manager", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Kevin Castillo", "address": "321 Pine St", "email": "kevinc@gmail.com", "position": "Assistant Store Manager", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Lauren Warwick", "address": "654 Elm Ave", "email": "lwarwick@yahoo.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Lindsey Heath", "address": "987 Birch Dr", "email": "jennydoe@gmail.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Jenny Rodriguez", "address": "135 Cedar St", "email": "jennyr@yahoo.com", "position": "Stock Associate", "availability": "Full-time", "department_name": "Stock Room"},
        {"name": "Hans Bas", "address": "246 Spruce Ave", "email": "hbas@yahoo.com", "position": "Stock Associate", "availability": "Part-time", "department_name": "Stock Room"},
        {"name": "Steven Pappas", "address": "369 Redwood Dr", "email": "stevenp@gmail.com", "position": "Security Officer", "availability": "Full-time", "department_name": "Security"},
        {"name": "Matthew George", "address": "147 Willow St", "email": "matthew@yahoo.com", "position": "Sales Associate", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Kurt Brock", "address": "56 Opal Dr", "email": "kurtbrock@yahoo.com", "position": "District Security Officer", "availability": "Full-time", "department_name": "Security"},
        {"name": "Briggette Nickal", "address": "39 Parkside St", "email": "bnickal@gmail.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Ash Ketchum", "address": "6 Victory Rd", "email": "ashketchumw@protonmail.com", "position": "Regional Security Officer", "availability": "Part-time", "department_name": "Security"},
        {"name": "Maximillion Pegasus", "address": "36 Grant St", "email": "maxp@yahoo.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Anthony Ventamiglia", "address": "234 Sunnyside Dr", "email": "antvent@gmail.com", "position": "Stock Associate", "availability": "Part-time", "department_name": "Stock Room"},
        {"name": "Julia Heather", "address": "467 Blackwood Rd", "email": "jheather@gmail.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Kevin Kincade", "address": "7 Oakwood Rd", "email": "kkincade@yahoo.com", "position": "Stock Associate", "availability": "Part-time", "department_name": "Stock Room"},
        {"name": "Kim Moss", "address": "5 Tea St", "email": "kmoss@departmentemail.com", "position": "District Store Manager", "availability": "Full-time", "department_name": "Sales Floor"},
        {"name": "Angelina Jolie", "address": "68 Montauk Rd", "email": "angjolie@yahoo.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"},
        {"name": "Jennifer Aniston", "address": "", "email": "janiston@yahoo.com", "position": "Sales Associate", "availability": "Part-time", "department_name": "Sales Floor"}
    ]

    for emp in employees:
        department = Department.query.filter_by(name=emp["department_name"]).first()
        if department:
            Employee.create(name=emp["name"], address=emp["address"], email=emp["email"], position=emp["position"], availability=emp["availability"], department_id=department.id)

def seed_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_departments()
        seed_employees()

if __name__ == "__main__":
    seed_db()

