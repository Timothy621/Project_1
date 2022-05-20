from flask_cors import CORS
from flask import Flask
import controllers.front_controller as fc

app = Flask(__name__)
CORS(app)
# Establish all the routes handled by Flask
fc.route(app)

if __name__ == '__main__':
    app.run()

