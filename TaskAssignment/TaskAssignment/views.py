"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from TaskAssignment import app, db
from models import Tasks, Persons

@app.route('/get_free_emps')
def get_free_emps():
    emps = Persons.query.filter(Persons.is_free == True).all()
    return jsonify(emps)

@app.route('/get_available_jobs')
def get_available_jobs():
    jobs = Tasks.query.filter(Tasks.completed==False).order_by(Tasks.created_at).all()
    return jsonify(jobs)
                              
@app.route('/mark_emp_busy/<emp_id>', methods=["POST"])
def toggle_emp_status(emp_id):
    emp = Persons.query.get(emp_id)
    if emp.is_free:
        emp.is_free = False
    else:
        emp.is_free = True
        
    db.session.commit()

@app.route('mark_task_completed/<task_id>', methods=["POST"])
def mark_task_completed(task_id):
    task = Tasks.query.get(task_id)
    tasks.completed = True
    db.session.commit()
    

'''
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
'''