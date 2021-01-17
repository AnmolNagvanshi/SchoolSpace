from app import db, admin
from datetime import datetime
from enum import Enum
from flask_admin.contrib.sqla import ModelView


class GenderType(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    registration_no = db.Column(db.String(255), unique=True, nullable=False)
    roll_no = db.Column(db.String(255), unique=True, nullable=True)
    father_name = db.Column(db.String(255), nullable=True)
    mother_name = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.Enum(GenderType), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    religion = db.Column(db.String(255), nullable=True)

    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    mobile_no = db.Column(db.String(32), nullable=False, unique=True, index=True)
    address = db.Column(db.String(512), nullable=True)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    pin_code = db.Column(db.String(255), nullable=False)

    photo = db.Column(db.String(512), nullable=True)
    tc = db.Column(db.String(512), nullable=True)
    migration = db.Column(db.String(512), nullable=True)

    username = db.Column(db.String(512), default='student', nullable=False)
    password = db.Column(db.String(512), default='student', nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


admin.add_view(ModelView(Student, db.session))
