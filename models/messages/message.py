from app import app, db
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    ADMIN = 'ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    receiver_id = db.Column(db.Integer, default=0, nullable=False, index=True)
    receiver_role = db.Column(db.Enum(UserRole), nullable=False)
    message = db.Column(db.String(2048), nullable=False)
    is_broadcast = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

