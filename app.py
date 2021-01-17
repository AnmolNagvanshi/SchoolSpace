from flask import Flask, request
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from marshmallow import ValidationError


app = FlaskAPI(__name__, static_url_path='')
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)
admin = Admin(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return err.messages, 400


@app.route('/')
def index():
    return "Hello World!"


@app.route('/test', methods=['POST', 'GET'])
def test():
    print(request.form)
    return request.form


from api.academic import assignment
import models

if __name__ == '__main__':
    app.run(debug=True)
