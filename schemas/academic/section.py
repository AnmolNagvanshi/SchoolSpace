from app import ma
from models.academic.section import Section
from marshmallow import post_load
from marshmallow.utils import EXCLUDE


class SectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Section
        load_only = ("password",)
        dump_only = ("id",)
        unknown = EXCLUDE

    @post_load
    def make_section(self, data, **kwargs):
        return Section(**data)

