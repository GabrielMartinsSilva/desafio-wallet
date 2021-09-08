#Teste
from wallet.utils import calculate_cashback


def test_calculate_cashback():

    cashback = calculate_cashback(
        [
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
        ]
    )

    assert cashback == 9.5
