from datetime import datetime
from exchanges.bitfinex import Bitfinex

price = None
fetched_at = None

def fetch():
    global price, fetched_at
    price = round(Bitfinex().get_current_price(), 2)
    fetched_at = datetime.now()
    print(f'    fetched new price: {price} ({fetched_at})')

def get():
    global fetched_at
    if price is None or fetched_at is None or (datetime.now() - fetched_at).seconds >= 60:
        fetch()
    return price