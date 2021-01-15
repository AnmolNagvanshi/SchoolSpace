from app import app, db
from flask import request
from models.users.student import Student
from models.academic.classes import Classes
from models.academic.section import Section
from schemas.users.student import StudentSchema
from werkzeug.utils import secure_filename
import os
from datetime import date

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


student_schema = StudentSchema()
student_list_schema = StudentSchema(many=True)


@app.route('/students', methods=['POST'])
def create_student():
    data = request.form
    student = student_schema.load(data)
    student.username = str(student.email)
    student.password = str(student.email)

    db.session.add(student)
    db.session.commit(student)
    return {"data": student_schema.dump(student)}, 200

    # year, month, day = dob.split('-')
    # today = date(int(year), int(month), int(day))

    # if tc:
    #     tc_filename = secure_filename(tc.filename)
    #     tc.save(os.path.join(app.config['UPLOAD_FOLDER_TC'], tc_filename))
    # else:
    #     tc_filename = None
    #
    # if migration:
    #     migration_filename = secure_filename(migration.filename)
    #     migration.save(os.path.join(app.config['UPLOAD_FOLDER_MIGRATION'], migration_filename))
    # else:
    #     migration_filename = None
    #
    # if photo:
    #     photo_filename = secure_filename(photo.filename)
    #     photo.save(os.path.join(app.config['UPLOAD_FOLDER_PHOTO'], photo_filename))
    # else:
    #     photo_filename = None


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
    return {"data": student_list_schema.dump(students)}, 200


@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student_section(student_id):
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
