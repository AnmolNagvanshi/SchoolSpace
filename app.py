from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError


app = Flask(__name__, static_url_path='')
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return err.messages, 400


from api.academic import assignment
import models

if __name__ == '__main__':
    app.run(debug=True)
