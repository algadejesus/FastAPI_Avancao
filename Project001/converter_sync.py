from os import getenv
import requests
from fastapi import HTTPException

ALPHAVENTEGE_APIKEY = getenv('ALPHAVENTEGE_APIKEY')

def sync_converter(from_currency: str, to_currencies: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currencies}&apikey={ALPHAVENTEGE_APIKEY}'
    
    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    print(response)
    
    data = response.json()
    print(data)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail='Realtime Currency Exchange Rate nat in response')
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    
    return price * exchange_rate