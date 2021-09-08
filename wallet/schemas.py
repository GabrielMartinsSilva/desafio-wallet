from marshmallow import Schema, ValidationError, fields, post_load, validate
from validate_docbr import CPF

product_type = {"A": 5, "B": 10, "C": 15}


class CustomerSchema(Schema):
    document = fields.Method(deserialize="validate_document")
    name = fields.Str()

    def validate_document(self, value, **kwargs):
        validator = CPF()

        if not validator.validate(value):
            raise ValidationError("Document invalid!")
        return value

class ProductSchema(Schema):
    type = fields.Str(
        required=True,
        validate=validate.OneOf(
            choices=product_type.keys(), error="Type not valid!"
        ),
    )
    value = fields.Float(required=True)
    qty = fields.Integer(required=True)


class CashbackSchema(Schema):
    total = fields.Float(required=True)
    sold_at = fields.DateTime(required=True)
    customer = fields.Nested(CustomerSchema)
    products = fields.List(fields.Nested(ProductSchema))

    @post_load
    def validate_total(self, data, **kwargs):
        aux = 0
        for item in data["products"]:
            aux += item["qty"] * item["value"]
        if aux != data["total"]:
            raise ValidationError("Total different then expected!", "total")
        return data
