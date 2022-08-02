from flask_sqlalchemy import *
from sqlalchemy import *

db=SQLAlchemy()

class Employee_Model(db.Model):
    __tablename__="Employee"

    employee_id= db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String())
    last_name=db.Column(db.String())
    gender=db.Column(db.String())
    email=db.Column(db.String())
    department=db.Column(db.String())
    tools=db.Column(db.String())

    def __init__(self, first_name, last_name, gender, email, department, tools):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.email=email
        self.department=department
        self.tools=tools
         
        def __repr__(self):
            return f"{self.first_name}:{self.last_name}"