from datetime import datetime
from enum import Enum

from app import db


class GenderType(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Teacher(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), nullable=False)
    designation = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum(GenderType), nullable=False)
    religion = db.Column(db.String(255), nullable=True)

    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    mobile_no = db.Column(db.String(20), nullable=False, unique=True, index=True)

    address = db.Column(db.String(512), nullable=True)
    joining_date = db.Column(db.Date, default=datetime.today, nullable=False)
    photo = db.Column(db.String(512), nullable=True)

    username = db.Column(db.String(512), default='teacher', nullable=False)
    password = db.Column(db.String(512), default='teacher', nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

