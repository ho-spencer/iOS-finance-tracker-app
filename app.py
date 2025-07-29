from flask import Flask

# Load .env into my Flask app
from dotenv import load_dotenv
import os
load_dotenv()       # Load environment variables from .env file

from config import Config   # Import Config

## ------- SERVER URL: http://127.0.0.1:5000/ 
app = Flask(__name__)               # create a Flask app instance
app.config.from_object(Config)      # Pass the Config class to Flask and load settings from config.py


# Route to appURL/ping to test the server
@app.route('/ping', methods = ["GET"])
def pint():
    return "PING WORKS"




if __name__ == "__main__":
    app.run(debug=True)