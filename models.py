'''
Defining models (in Flask using SQLAlchemy) to represent the tables in my database (aka: creating a Python classes to represent each table in the database)
- each class inherits db.Model class to define models

From app.py, using the import 'from flask_sqlalchemy import SQLAlchemy' gives me access to the SQLAlchemy column types (db.Integer, db.Text, db.Date, etc.).
The parameters in db.Column matches my tables' setup in pgAdmin (postgreSQL).
'''



from app import db
from datetime import datetime       # used for the created_at column (when user created their account for the app)
from sqlalchemy import func         # used to set the server_default "default" param in the 'created_at' column
from sqlalchemy.dialects.postgresql import ARRAY    # used for a column where the data type is an array of text


'''
Represents the "users" table in the database
- 'id' column is a primary key
- 'email' column must be unique
- 'created_at' column uses timezone and default value of now()
'''
class Users(db.Model):
    __tablename__ = 'users'     # Map this Users class to the 'users' table
    id = db.Column(db.Integer, nullable = False, primary_key = True)       # id Column
    email = db.Column(db.Text, nullable = False, unique = True)            # email Column
    password = db.Column(db.Text, nullable = False)                        # password Column
    created_at = db.Column(db.DateTime(timezone = True), nullable = False, server_default = func.now())    # created_at Column


'''
Represents the 'transactions' table in the database
- 'id' column is a primary key and must be unique
- 'user_id' column is a foreign key that links the user_id column to the 'id' column in the 'users' table
- 'transaction_amount' column can have 10 total digits with a precision of 2 numbers to the right of the decimal point
- 'plaid_id' must be unique
'''
class Transactions(db.Model):
    __tablename__ = 'transactions'      # Map this Transactions class to the 'transactions' table 
    id = db.Column(db.Integer, nullable = False, primary_key = True, unique = True) # id column
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)    # user_id column
    account_id = db.Column(db.Text, nullable = False)                               # account_id column
    transaction_name = db.Column(db.Text, nullable = False)                         # transaction_name column
    transaction_amount = db.Column(db.Numeric(10, 2), nullable = False)             # transaction_amount column
    transaction_date = db.Column(db.Date, nullable = False)                         # transaction_date column
    transaction_category = db.Column(ARRAY(db.Text), nullable = False)              # transaction_category column
    transaction_type = db.Column(db.Text, nullable = False)                         # transaction_type column
    plaid_id = db.Column(db.Text, nullable = False, unique = True)                  # plaid_id column
