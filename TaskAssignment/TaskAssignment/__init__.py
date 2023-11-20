"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import TaskAssignment.views

#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:5876/database_name'


db = SQLAlchemy(app)