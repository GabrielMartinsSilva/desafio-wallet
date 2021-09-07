import pytest
from marshmallow import ValidationError

from wallet.schemas import CashbackSchema, CustomerSchema, ProductSchema


@pytest.fixture(scope="function")
def schema():
    return ProductSchema()


@pytest.fixture(scope="function")
def customerschema():
    return CustomerSchema()


def test_simple(schema):
    data_sample = {"type": "l", "value": 50, "qty": 8}
    with pytest.raises(ValidationError, match="Type not valid!"):
        schema.load(data_sample)


def test_validate_document(customerschema):
    data_sample = {"document": "40221945882", "name": "Gabriel"}

    with pytest.raises(ValidationError, match="Document invalid!"):
        customerschema.load(data_sample)


def test_validate_date():
    schema = CashbackSchema(only=["sold_at"])

    data_sample = {"sold_at": "20/05/1995"}
    with pytest.raises(ValidationError, match="Not a valid datetime."):
        schema.load(data_sample)


def test_cashback():
    schema = CashbackSchema()

    data_sample = {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "40221945881",
            "name": "JOSE DA SILVA",
        },
        "total": "10.00",
        "products": [
            {
                "type": "A",
                "value": "10.00",
                "qty": 1,
            },
            {
                "type": "B",
                "value": "10.00",
                "qty": 9,
            },
        ],
    }
    with pytest.raises(ValidationError, match="Total different then expected!"):
        schema.load(data_sample)
