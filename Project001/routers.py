from fastapi import APIRouter
from converter_sync import sync_converter

router = APIRouter()

# # Path parameter
# @router.get('/converter/{from_currency}')
# def converter(from_currency: str):
#     return "It works"

# Query parameter
@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')
    
    print(to_currencies);
    
    result = []
    
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currencies=currency,
            price=price
        )
        
        result.append(response)
        
    return result