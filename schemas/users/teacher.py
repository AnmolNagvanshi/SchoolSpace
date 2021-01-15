from app import ma
from models.users.teacher import Teacher
from marshmallow import post_load
from marshmallow.utils import EXCLUDE


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        load_only = ("password",)
        dump_only = ("id", 'created_at', 'updated_at')
        unknown = EXCLUDE

    @post_load
    def make_teacher(self, data, **kwargs):
        return Teacher(**data)

