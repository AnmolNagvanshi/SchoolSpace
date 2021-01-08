from app import db
from datetime import datetime
from enum import Enum


class GenderType(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    registration_no = db.Column(db.String(255), nullable=False)
    roll_no = db.Column(db.String(255), nullable=True)
    father_name = db.Column(db.String(255), nullable=True)
    mother_name = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.Enum(GenderType), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    religion = db.Column(db.String(255), nullable=True)

    email = db.Column(db.String(255), nullable=True)
    mobile_no = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(512), nullable=True)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    pin_code = db.Column(db.String(255), nullable=False)

    photo_path = db.Column(db.String(512), nullable=True)
    tc_path = db.Column(db.String(512), nullable=True)
    migration_path = db.Column(db.String(512), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
