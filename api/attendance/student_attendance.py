from flask import request
from app import app, db
from models.attendance.student_attendance import StudentAttendance, Status
from models.academic.classes import Classes
from models.academic.section import Section
from models.users import Student

from collections import defaultdict
from datetime import date


MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


@app.route('/students/<int:student_id>/attendance', methods=['POST'])
def create_attendance_by_student_id(student_id):
    if not Student.query.filter_by(id=student_id).first():
        return {"message": "student does not exist"}, 404


# @app.route('/students/<int:student_id>/attendance', methods=['GET'])
# def get_attendance_by_student_id(student_id):
#     if not Student.query.filter_by(id=student_id).first():
#         return {"message": "student does not exist"}, 404
#     records = StudentAttendance.query.filter_by(student_id=student_id).order_by().all()
#     arr = []
#
#     res = dict()
#     for month in MONTHS:
#         res[month] = []
#
#     for record in records:
#         json = {'id': record.id, 'date': record.date, 'status': record.status}
#         arr.append(json)
#
#     return {"data": arr}, 200


@app.route('classes/<int:class_id>/sections/<int:section_id>/students/attendance', methods=['POST'])
def create_student_attendance_records(class_id, section_id):
    if not Classes.query.filter_by(id=class_id).first():
        return {"message": f"class with id={class_id} does not exist"}, 404

    if not Section.query.filter_by(id=section_id, class_id=class_id).first():
        return {"message": f"section with id={section_id} does not exist for this class"}

    data = request.form
    today = request.form.get('date', date.today())
    data.pop('date')

    rows = []
    for student_id, status in data.items():
        record = StudentAttendance(student_id=int(student_id), status=Status(status), date=today)
        rows.append(record)

    db.session.bulk_save_objects(rows)
    db.session.commit()
    return {"message": "Student attendance records saved"}, 201
