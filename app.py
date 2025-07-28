from flask import Flask

# Load .env into my Flask app
from dotenv import load_dotenv
import os

load_dotenv()

## ------- SERVER URL: http://127.0.0.1:5000/ 
app = Flask(__name__)       # create a Flask app instance


# Route to appURL/ping to test the server
@app.route('/ping', methods = ["GET"])
def pint():
    return "PING WORKS"




if __name__ == "__main__":
    app.run(debug=True)