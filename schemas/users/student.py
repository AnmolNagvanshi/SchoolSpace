from app import ma
from models.users.student import Student
from marshmallow import post_load
from marshmallow.utils import EXCLUDE


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_only = ("password",)
        dump_only = ("id", "created_at", "updated_at", 'class_id', 'section_id')
        unknown = EXCLUDE

    @post_load
    def make_student(self, data, **kwargs):
        return Student(**data)

