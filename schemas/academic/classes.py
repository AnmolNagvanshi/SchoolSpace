from app import ma
from models.academic.classes import Classes
from marshmallow import post_load
from marshmallow.utils import EXCLUDE


class ClassesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Classes
        load_only = ("password",)
        dump_only = ("id",)
        unknown = EXCLUDE

    @post_load
    def make_classes(self, data, **kwargs):
        return Classes(**data)

