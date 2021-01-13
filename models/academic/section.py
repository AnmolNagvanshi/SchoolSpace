from app import db
from datetime import datetime


class Section(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    head_teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    name = db.Column(db.String(6), nullable=False, unique=True, index=True)
    strength = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

