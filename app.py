from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy     # Initialize SQLAlchemy
from flask_migrate import Migrate           # Flask-Migrate

# Load .env into my Flask app
from dotenv import load_dotenv
import os
load_dotenv()       # Load environment variables from .env file

from config import Config   # Import Config

## ------- SERVER URL: http://127.0.0.1:5000/ 
app = Flask(__name__)               # create a Flask app instance
app.config.from_object(Config)      # Pass the Config class to Flask and load settings from config.py

db = SQLAlchemy(app)                # Bind SQLAlchemy to my Flask App (db oject)
                                    # passing in "app" allows SQLAlchemy to read the app's config setup from config.py
                                    # db object is an instance of the SQLAlchemy class from flask_sqlalchemy

migrate = Migrate(app, db)          # connect Flask-Migrate to the Flask app (app) and SQLAlchemy database (db)

# Route to appURL/ping to test the server
@app.route('/ping', methods = ["GET"])
def print():
    return "PING WORKS"

'''
=======================
*   MAIN APP ROUTES   *
=======================
'''
# Login Route
@app.route("/applogin", methods = ["POST"])
def applogin():
    login_data = request.get_json()             # use requset.get_json() to read the JSON sent in the POST request
    username = login_data.get("username")       # get the username
    password = login_data.get("password")       # get the password

    #--- VALIDATE LOGIN HERE ---


# Link Bank Route


# Get Daily Transactions Route


# Get Weekly Transactions Route


# Get Monthly Transactions Route






if __name__ == "__main__":
    app.run(debug=True)