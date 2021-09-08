from django.urls import reverse
import pytest


@pytest.fixture
def sale_data():
    return {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "40221945881",
            "name": "JOSE DA SILVA",
        },
        "total": "100.00",
        "products": [
            {
                "type": "A",
                "value": 10.00,
                "qty": 1,
            },
            {
                "type": "B",
                "value": 10.00,
                "qty": 9,
            },
        ],
    }


@pytest.mark.django_db
def test_view(client, sale_data):
    url = reverse("cashback")
    import json
    response = client.post(
        url, data=json.dumps(sale_data), content_type="application/json"
    )
    assert response.status_code == 200
