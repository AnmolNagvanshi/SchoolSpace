from app import db


class TeachersTimeTable(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.ForeignKey('teachers.id'), index=True, nullable=False)
    class_1 = db.Column(db.String(64), nullable=True)
    class_2 = db.Column(db.String(64), nullable=True)
    class_3 = db.Column(db.String(64), nullable=True)
    class_4 = db.Column(db.String(64), nullable=True)
    remaining_slots = db.Column(db.Integer, default=0, nullable=False)
