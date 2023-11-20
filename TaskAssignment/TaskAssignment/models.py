from TaskAssignment import db

class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    is_free = db.Column(db.Boolean, unique=False, default=True)
    
    def __repr__(self):
        return f'<Employee {self.firstname}>'
    
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    completed = db.Column(db.Boolean, unique=False, default=False)
    
    def __repr__(self):
        return f'<Employee {self.name}>'