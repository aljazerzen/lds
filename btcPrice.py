from datetime import datetime
from exchanges.bitfinex import Bitfinex

price = None
priceFetched = None

def fetchPrice():
    global price, priceFetched
    price = round(Bitfinex().get_current_price(), 2)
    priceFetched = datetime.now()
    print(f'fetched new price: {price} ({priceFetched})')

def getPrice():
    if price is None or priceFetched is None or (datetime.now() - priceFetched).seconds >= 60:
        fetchPrice()
    return price