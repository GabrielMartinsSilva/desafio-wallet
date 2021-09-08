import json

import requests
from django.http import JsonResponse
from marshmallow import ValidationError

from wallet.models import Cashback
from wallet.schemas import CashbackSchema
from wallet.utils import calculate_cashback


def cashback(request):

    if request.method == "POST":
        schema_write = CashbackSchema()
        data = json.loads(request.body.decode())

        try:
            data = schema_write.load(data)
            model = Cashback(**data)
            model.save()
        except ValidationError as err:
            return JsonResponse(err.messages, status=422)
    
    customer_document = data["customer"]["document"]
    
    cashback_value = calculate_cashback(data["products"])
    url = "https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback"
    data = {"document": customer_document, "cashback": cashback_value}
    response = requests.post(url, data)

    return JsonResponse(response.json(), status=200)
