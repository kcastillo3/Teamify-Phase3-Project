from config import db

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    position = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    department = db.relationship("Department", backref=db.backref("employees", lazy=True))

    @classmethod
    def create(cls, name, address, email, position, availability, department_id):
        if cls.query.filter_by(email=email).first():
            print(f"Employee with email '{email}' already exists.")
            return None

        new_employee = cls(name=name, address=address, email=email, position=position, availability=availability, department_id=department_id)
        try:
            db.session.add(new_employee)
            db.session.commit()
            return new_employee
        except Exception as e:  
            db.session.rollback()
            print(f"Error creating employee: {e}")
            return None

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, employee_id):
        return cls.query.get(employee_id)

    @classmethod
    def delete(cls, employee_id):
        employee = cls.find_by_id(employee_id)
        if employee:
            try:
                db.session.delete(employee)
                db.session.commit()
            except Exception as e:  
                db.session.rollback()
                print(f"Error deleting employee: {e}")

    def update(self, name=None, address=None, email=None, position=None, availability=None):
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if position is not None:
            self.position = position
        if availability is not None:
            self.availability = availability
        try:
            db.session.commit()
        except Exception as e:  
            db.session.rollback()
            print(f"Error updating employee: {e}")

    def __repr__(self):
        return f"Employee(Id: {self.id}, Name: {self.name}, Email: {self.email}, Position: {self.position}, Availability: {self.availability})"

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    @classmethod
    def create(cls, name):
        if cls.query.filter_by(name=name).first():
            print(f"Department '{name}' already exists.")
            return None
        new_department = cls(name=name)
        try:
            db.session.add(new_department)
            db.session.commit()
            return new_department
        except Exception as e:  
            db.session.rollback()
            print(f"Error creating department: {e}")
            return None

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, department_id):
        return cls.query.get(department_id)

    @classmethod
    def delete(cls, department_id):
        department = cls.find_by_id(department_id)
        if department and department.employees:
            print("Cannot delete department with employees.")
            return
        if department:
            try:
                db.session.delete(department)
                db.session.commit()
            except Exception as e:  
                db.session.rollback()
                print(f"Error deleting department: {e}")

    def __repr__(self):
        return f"Department(Id: {this.id}, Name: {this.name})"


