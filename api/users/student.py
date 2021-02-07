from typing import Optional

from app import app, db
from flask import request
from models.users.student import Student
from models.academic.classes import Classes
from models.academic.section import Section
from schemas.users.student import StudentSchema
from werkzeug.utils import secure_filename
import os
from datetime import date

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'mp4'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


student_schema = StudentSchema()
student_list_schema = StudentSchema(many=True)


@app.route('/classes/<int:class_id>/sections/<int:section_id>/students', methods=['POST'])
def create_student(class_id, section_id):
    if not Classes.query.filter_by(id=class_id).first():
        return {"message": f"class with id={class_id} does not exist"}, 404

    if not Section.query.filter_by(id=section_id, class_id=class_id).first():
        return {"message": f"section with id={section_id} does not exist for this class"}

    data = request.form
    student = student_schema.load(data)
    student.class_id = class_id
    student.section_id = section_id

    student.username = str(student.email)
    student.password = str(student.email)

    tc = request.files.get('tc')
    migration = request.files.get('migration')
    photo = request.files.get('photo')

    save_file(tc, 'TC')
    save_file(migration, 'MIGRATION')
    save_file(photo, 'PHOTO')

    student.tc = tc.filename if tc else None
    student.migration = migration.filename if migration else None
    student.photo = photo.filename if photo else None

    db.session.add(student)
    db.session.commit()

    set_file_paths(student)
    # student.tc = get_file_path(request.files.get('tc'), 'TC')
    # student.migration = get_file_path(request.files.get('migration'), 'MIGRATION')
    # student.photo = get_file_path(request.files.get('photo'), 'PHOTO')

    return {"data": student_schema.dump(student)}, 200


@app.route('/classes/<int:class_id>/sections/<int:section_id>/students', methods=['GET'])
def get_all_students_by_class_and_section(class_id, section_id):
    if not Classes.query.filter_by(id=class_id).first():
        return {"message": f"class with id={class_id} does not exist"}, 404

    if not Section.query.filter_by(id=section_id, class_id=class_id).first():
        return {"message": f"section with id={section_id} does not exist for this class"}

    students = (Student.query
                .filter_by(class_id=class_id, section_id=section_id)
                .order_by(Student.registration_no.desc())
                .all()
                )

    for student in students:
        set_file_paths(student)

    return {"data": student_list_schema.dump(students)}, 200


@app.route('/students/<int:student_id>')
def get_student_by_id(student_id):
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        return {"message": f"student with id={student_id} does not exist"}, 404

    set_file_paths(student)
    return {"data": student_schema.dump(student)}, 200


@app.route('/classes/<int:class_id>/sections/<int:section_id>/students/<int:student_id>', methods=['PATCH'])
def update_student_section(class_id, section_id, student_id):
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        return {"message": f"Student with id={student_id} does not exist"}, 404

    new_section_id = request.form.get('section', None)
    if not new_section_id:
        return {"message": "Missing section property"}, 404

    student.section_id = new_section_id
    db.session.add(student)
    db.session.commit()

    return {"message": "Student's section updated successfully"}, 200


def save_file(file, file_type: str):
    if not file:
        return
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER_' + file_type], filename))


def get_file_path(filename: str, file_type: str) -> Optional[str]:
    if not filename:
        return None
    return '/static/' + os.path.join(app.config['UPLOAD_FOLDER_' + file_type]) + '/' + filename


def set_file_paths(student: Student):
    student.tc = get_file_path(student.tc, 'TC')
    student.migration = get_file_path(student.migration, 'MIGRATION')
    student.photo = get_file_path(student.photo, 'PHOTO')
