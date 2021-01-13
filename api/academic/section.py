from app import app, db
from flask import request
from models.academic.classes import Classes
from models.academic.section import Section
from schemas.academic.section import SectionSchema

section_schema = SectionSchema()
section_list_schema = SectionSchema(many=True)


@app.route('/classes/<int:class_id>/sections', methods=['POST'])
def create_section(class_id):
    class_obj = Classes.query.filter_by(id=class_id).first()
    if not class_obj:
        return {"message": f"class with id={class_id} not found"}, 404

    data = request.form
    section = section_schema.load(data)
    class_obj.sections.append(section)
    db.session.commit()
    return {"data": section_schema.dump(section)}, 201


@app.route('/classes/<int:class_id>/sections', methods=['GET'])
def get_all_sections_by_class_id(class_id):
    class_obj = Classes.query.filter_by(id=class_id).first()
    if not class_obj:
        return {"message": f"class with id={class_id} not found"}, 404
    sections = section_list_schema.dump(class_obj.sections)
    return {"data": sections}, 200

