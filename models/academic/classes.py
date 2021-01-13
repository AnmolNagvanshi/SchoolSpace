from app import db
from datetime import datetime


class Classes(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(6), nullable=False, unique=True, index=True)
    numeric = db.Column(db.Integer, nullable=False, unique=True, index=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    sections = db.relationship('Section', backref='class_obj', lazy='dynamic')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

