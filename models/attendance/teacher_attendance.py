from app import db
from enum import IntEnum
from datetime import date


class Status(IntEnum):
    ABSENT = 0
    HALF_DAY = 1
    PRESENT = 2

class TeacherAttendance(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('student.id'), index=True, nullable=False)
    date = db.Column(db.Date, default=date.today, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
