from flask import request
from app import app, db
from models.academic.classes import Classes
from schemas.academic.classes import ClassesSchema

class_schema = ClassesSchema()
class_list_schema = ClassesSchema(many=True)


@app.route('/classes', methods=['POST'])
def create_class():
    data = request.form
    if Classes.query.filter_by(name=data['name']).first():
        return {"message": "name is not unique"}, 400

    if Classes.query.filter_by(numeric=int(data['numeric'])).first():
        return {"message": "numeric is not unique"}, 400

    class_obj = class_schema.load(data)
    db.session.add(class_obj)
    db.session.commit()
    return {"data": class_schema.dump(class_obj)}, 201


@app.route('/classes', methods=['GET'])
def get_all_classes():
    numeric = request.args.get('numeric', None)
    if numeric:
        class_obj = Classes.query.filter_by(numeric=int(numeric)).first()
        return {"data": class_schema.dump(class_obj)}, 200
    else:
        classes = Classes.query.all()
        return {"data": class_list_schema.dump(classes)}, 200


@app.route('/classes/<int:class_id>', methods=['GET'])
def get_class_by_id(class_id):
    class_obj = Classes.query.filter_by(id=class_id).first()
    if not class_obj:
        return {"message": f"class with id={class_id} not found"}, 404
    return {"data": class_schema.dump(class_obj)}, 200

