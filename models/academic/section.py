from app import db, admin
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from models.academic.classes import Classes
from models.users import Teacher

class Section(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    head_teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    name = db.Column(db.String(6), nullable=False, unique=True, index=True)
    strength = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    class_obj = db.relationship('Classes', backref='sections')
    head_teacher = db.relationship('Teacher', backref='main_class')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


admin.add_view(ModelView(Section, db.session))
