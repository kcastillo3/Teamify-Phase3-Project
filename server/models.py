from config import db

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) 
    address = db.Column(db.String)  
    email = db.Column(db.String, nullable=False, unique=True)  
    position = db.Column(db.String, nullable=False)  
    availability = db.Column(db.String)  

    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False) 
  
    department = db.relationship("Department", backref=db.backref("employees", lazy=True))

    def __repr__(self):
        return (
            f"Employee(Id: {self.id}, Name: {self.name}, Address: {self.address}, "
            f"Email: {self.email}, Position: {self.position}, Availability: {self.availability})"
        )

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  

    def __repr__(self):
        return f"Department(Id: {self.id}, Name: {self.name})"