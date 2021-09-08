from wallet.schemas import product_type


def calculate_cashback(products):
    cashback = 0
    for item in products:
        cashback += (item["value"] * item["qty"]) * (product_type[item["type"]] / 100)
    return cashback
