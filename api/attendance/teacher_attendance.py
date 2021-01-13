from flask import request
from app import app, db
from models.attendance.teacher_attendance import TeacherAttendance, Status
from models.users import Teacher


@app.route('/teachers/<int:student_id>/attendance', methods=['GET'])
def get_attendance_by_teacher_id(student_id):
    if not Teacher.query.filter_by(id=student_id).first():
        return {"message": "teacher does not exist"}, 404
    records = TeacherAttendance.query.filter_by(student_id=student_id).all()
    arr = []
    for record in records:
        json = {'id': record.id, 'date': record.date, 'status': record.status}
        arr.append(json)
    return {"data": arr}, 200


@app.route('/teachers/attendance', methods=['POST'])
def create_teacher_attendance_records():
    data = request.get_json()
    rows = []
    for t_id, s in data.items():
        record = TeacherAttendance(teacher_id=int(t_id), status=Status(s))
        rows.append(record)
    db.session.bulk_save_objects(rows)
    db.session.commit()
    return {"message": "Teacher attendance records saved"}, 201
