import os
from typing import Optional

from werkzeug.utils import secure_filename

from app import app, db
from flask import request
from datetime import date
from models.users.teacher import Teacher
from schemas.users.teacher import TeacherSchema
from models.academic.classes import Classes

teacher_schema = TeacherSchema()
teacher_list_schema = TeacherSchema(many=True)


@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.form
    teacher = teacher_schema.load(data)

    if Teacher.query.filter_by(email=data['email']).first():
        return {"message": "email is not unique"}, 400

    if Teacher.query.filter_by(email=data['mobile_no']).first():
        return {"message": "mobile no is not unique"}, 400

    photo = request.files.get('photo')
    if photo:
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER_PHOTO'], photo_filename))
        teacher.photo = photo_filename

    teacher.username = str(teacher.email)
    teacher.password = str(teacher.password)
    db.session.add(teacher)
    db.session.commit()

    teacher.photo = get_file_path(teacher.photo)
    new_teacher = teacher_schema.dump(teacher)
    return {"data": new_teacher}, 201


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    teachers = Teacher.query.all()
    for teacher in teachers:
        teacher.photo = get_file_path(teacher.photo)
    return {"data": teacher_list_schema.dump(teachers)}, 200


@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    teacher = Teacher.query.filter_by(id=id).first()
    if not teacher:
        return {"message": f"Teacher with id={id} does not exist"}, 404

    teacher.photo = get_file_path(teacher.photo)
    return {"data": teacher_schema.dump(teacher)}, 200


def get_file_path(photo) -> Optional[str]:
    if photo:
        return 'static/' + os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP']) + '/' + photo
    return None
