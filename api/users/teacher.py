import os

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

    teacher.username = str(teacher.email)
    teacher.password = str(teacher.password)
    db.session.add(teacher)
    db.session.commit()

    return {"data": teacher_schema.dump(teacher)}, 201


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    teachers = Teacher.query.all()
    return {"data": teacher_list_schema.dump(teachers)}, 200

    # if teachers:
    #     for teacher in teachers:
    #         if teacher.photo:
    #             file_path = 'static/' + os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP']) + '/' + teacher.photo
    #         else:
    #             file_path = None
    #         obj = {"name": teacher.name, "gender": teacher.gender, "mobile": teacher.mobile, "address": teacher.address,
    #                "father_name": teacher.father_name, "photo": file_path, "dob": teacher.dob}
    #         res.append(obj)
    #     return {"message": res}, 200


@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    teacher = Teacher.query.filter_by(id=id).first()
    if not teacher:
        return {"message": f"Teacher with id={id} does not exist"}, 404
    return {"data": teacher_schema.dump(teacher)}, 200
    # if teachers:
    #     for teacher in teachers:
    #         if teacher.photo:
    #             file_path = 'static/' + os.path.join(app.config['UPLOAD_FOLDER_TEACHER_DP']) + '/' + teacher.photo
    #         else:
    #             file_path = None
    #         obj = {"name": teacher.name, "gender": teacher.gender, "mobile": teacher.mobile, "address": teacher.address,
    #                "father_name": teacher.father_name, "photo": file_path, "dob": teacher.dob}
    #         res.append(obj)
    #     return {"message": res}, 200
    # else:
    #     return {"message": "No teachers registered yet"}, 200


# @app.route('/assign-class', methods=['POST'])
# def assign_class():
#     teacher_id = request.form.get('teacher_id', None)
#     class_id = request.form.get('class_id', None)
#
#     if not all((teacher_id, class_id)):
#         return {"message": "All fields are required"}, 404
#     else:
#         class_obj = Classes.query.filter_by(id=class_id).first()
#         flag = 0
#
#         if class_obj:
#             if class_obj.teacher_id:
#                 flag = flag + 1
#             else:
#                 pass
#
#             if flag == 0:
#                 class_obj.teacher_id = teacher_id
#                 db.session.commit()
#                 return {"message": "Teacher assigned"}, 200
#             else:
#                 return {"message": "Another teacher already present in this class"}, 404
#         else:
#             return {"message": "Invalid class"}, 404
