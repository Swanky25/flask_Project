import re
import string
from flask import Flask, request, render_template, redirect
from sqlalchemy import false
from models import db,Employee_Model

app=Flask(__name__)

#database connection
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Employee.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
db.init_app(app)

#to create the table
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('create.html')
    if request.method=='POST':
        Tools=request.form.getlist('tools')
        tools=",".join(map(str,Tools))
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        gender=request.form['gender']
        email=request.form['email']
        
        department=request.form['Department']
        tools=tools

        employee=Employee_Model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            department=department,
            tools=tools
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')

@app.route('/', methods=['GET'])
def retrieveList():
    Employee=Employee_Model.query.all()
    return render_template('index.html', employee=Employee)

@app.route('/<int:employee_id>/delete', methods=['GET', 'POST'])
def delete(employee_id):
    employees=Employee_Model.query.filter_by(employee_id=employee_id).first()
    if request.method=='POST':
            if employees:
                db.session.delete(employees)
                db.session.commit()
                return redirect("/')
            abort(404)
    return render_template('delete.html')    

@app.route('/<int:employee_id>/edit', methods=['GET', 'POST'])
def edit(employee_id):
    employees=Employee_Model.query.filter_by(employee_id=employee_id).first()
    if request.method=='POST':
        db.session.delete(employees)
        db.session.commit()
        if employees:
            Tools=request.form.getlist('tools')
            tools=",".join(map(str,Tools))
            first_name=request.form['first_name']
            last_name=request.form['last_name']
            gender=request.form['gender']
            email=request.form['email']
            
            department=request.form['Department']
            tools=tools

            employee=Employee_Model(
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                department=department,
                tools=tools
            )
            db.session.add(employee)
            db.session.commit()
            return redirect('/')
        return f"employee with id= {employee_id} does not exist"

    return render_template('edit.html', employee=employees)




app.run(debug=True, port = 7777)