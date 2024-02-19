from config import db, app
from models import Department, Employee

def create_tables():
    with app.app_context():
        db.create_all()

def clear_tables():
    with app.app_context():
        Employee.query.delete()
        Department.query.delete()
        db.session.commit()

def seed_departments():
    with app.app_context():
        department1 = Department(name="Sales Floor")
        department2 = Department(name="Stock Room")
        department3 = Department(name="Security")

        db.session.add(department1)
        db.session.add(department2)
        db.session.add(department3)
        db.session.commit()

def seed_employees():
    with app.app_context():
        department1 = Department.query.filter_by(name="Sales Floor").first()
        department2 = Department.query.filter_by(name="Stock Room").first()
        department3 = Department.query.filter_by(name="Security").first()

        employee1 = Employee(name="Jubin Luke", address="123 Main St", email="jb@gmail.com", position="Store Manager", availability="Full-time", department_id=department1.id)
        employee2 = Employee(name="Megan Black", address="456 Maple Ave", email="meganb@yahoo.com.com", position="Assistant Store Manager in Training", availability="Full-time", department_id=department1.id)
        employee3 = Employee(name="Caleb O'Leary", address="789 Oak Dr", email="olearycaleb@protonmail.com", position="Assistant Store Manager", availability="Full-time", department_id=department1.id)
        employee4 = Employee(name="Kevin Castillo", address="321 Pine St", email="kevinc@gmail.com", position="Assistant Store Manager", availability="Full-time", department_id=department1.id)
        employee5 = Employee(name="Lauren Warwick", address="654 Elm Ave", email="lwarwick@yahoo.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee6 = Employee(name="Lindsey Heath", address="987 Birch Dr", email="jennydoe@gmail.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee7 = Employee(name="Jenny Rodriguez", address="135 Cedar St", email="jennyr@yahoo.com", position="Stock Associate", availability="Full-time", department_id=department2.id)
        employee8 = Employee(name="Hans Bas", address="246 Spruce Ave", email="hbas@yahoo.com", position="Stock Associate", availability="Part-time", department_id=department2.id)
        employee9 = Employee(name="Steven Pappas", address="369 Redwood Dr", email="stevenp@gmail.com", position="Security Officer", availability="Full-time", department_id=department3.id)
        employee10 = Employee(name="Matthew George", address="147 Willow St", email="matthew@yahoo.com", position="Sales Associate", availability="Full-time", department_id=department1.id)
        employee11 = Employee(name="Kurt Brock", address="56 Opal Dr", email="kurtbrock@yahoo.com", position="District Security Officer", availability="Full-time", department_id=department3.id)
        employee12 = Employee(name="Briggette Nickal", address="39 Parkside St", email="bnickal@gmail.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee13 = Employee(name="Ash Ketchum", address="6 Victory Rd", email="ashketchumw@prototonmail.com", position="Regional Security Officer", availability="Part-time", department_id=department3.id)
        employee14 = Employee(name="Maximillion Pegasus", address="36 Grant St", email="maxp@yahoo.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee15 = Employee(name="Anthony Ventamiglia", address="234 Sunnyside Dr", email="antvent@gmail.com", position="Stock Associate", availability="Part-time", department_id=department1.id)
        employee16 = Employee(name="Julia Heather", address="467 Blackwood Rd", email="jheather@gmail.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee17 = Employee(name="Kevin Kincade", address="7 Oakwood Rd", email="kkincade@yahoo.com", position="Stock Associate", availability="Part-time", department_id=department2.id)
        employee18 = Employee(name="Kim Moss", address="5 Tea St", email="kmoss@departmentemail.com", position="District Store Manager", availability="Full-time", department_id=department1.id)
        employee19 = Employee(name="Angelina Jolie", address="68 Montauk Rd", email="angjolie@yahoo.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        employee20 = Employee(name="Jennifer Aniston", address="", email="janiston@yahoo.com", position="Sales Associate", availability="Part-time", department_id=department1.id)
        
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.add(employee3)
        db.session.add(employee4)
        db.session.add(employee5)
        db.session.add(employee6)
        db.session.add(employee7)
        db.session.add(employee8)
        db.session.add(employee9)
        db.session.add(employee10)
        db.session.add(employee11)
        db.session.add(employee12)
        db.session.add(employee13)
        db.session.add(employee14)
        db.session.add(employee15)
        db.session.add(employee16)
        db.session.add(employee17)
        db.session.add(employee18)
        db.session.add(employee19)
        db.session.add(employee20)

        db.session.commit()

def seed_db():
    with app.app_context():
        db.drop_all()  # Drop all tables
        db.create_all()  # Create all tables
        seed_departments()  # Seed the departments
        seed_employees()  # Seed the employees
        db.session.commit()  # Commit the changes

if __name__ == "__main__":
    seed_db()
