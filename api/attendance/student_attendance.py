from flask import request
from app import app, db
from models.attendance.student_attendance import StudentAttendance, Status
from models.users import Student


@app.route('/students/<int:student_id>/attendance', methods=['GET'])
def get_attendance_by_student_id(student_id):
    if not Student.query.filter_by(id=student_id).first():
        return {"message": "student does not exist"}, 404
    records = StudentAttendance.query.filter_by(student_id=student_id).all()
    arr = []
    for record in records:
        json = {'id': record.id, 'date': record.date, 'status': record.status}
        arr.append(json)
    return {"data": arr}, 200


@app.route('/students/attendance', methods=['POST'])
def create_student_attendance_records():
    data = request.get_json()
    rows = []
    for student_id, status in data.items():
        record = StudentAttendance(student_id=int(student_id), status=Status(status))
        rows.append(record)
    db.session.bulk_save_objects(rows)
    db.session.commit()
    return {"message": "Student attendance records saved"}, 201
