from app import ma
from models.academic.classes import Classes
from marshmallow import post_load
from marshmallow.utils import EXCLUDE


class ClassesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Classes
        dump_only = ("id", 'created_at', 'updated_at')
        unknown = EXCLUDE

    @post_load
    def make_classes(self, data, **kwargs):
        return Classes(**data)

