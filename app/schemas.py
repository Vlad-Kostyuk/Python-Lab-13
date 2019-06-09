from marshmallow import fields, Schema
from marshmallow import post_load
from marshmallow_enum import EnumField

from .config import marsh
from .models import Clothing, Producer, Season, FishingSetType, Sex, Size


class ClothingRawSchema(Schema):
    UPDATE_FIELDS = [
        "price",
        "name",
        "material",
        "producer",
        "guarantee",
        "color",
        "season",
        "fishing_set_type",
        "size",
        "sex",
    ]

    id = fields.Integer()
    price = fields.Integer()
    name = fields.String()
    material = fields.String()
    producer = EnumField(Producer)
    guarantee = fields.Integer()
    color = fields.String()
    season = EnumField(Season)
    fishing_set_type = EnumField(FishingSetType)
    size = EnumField(Size)
    sex = EnumField(Sex)


class ClothingSchema(ClothingRawSchema):
    @post_load
    def make_clothing(self, data):
        return Clothing(**data)
