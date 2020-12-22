from datetime import datetime, timedelta

from sp_api.api import Orders
from sp_api.base import SellingApiException


def test_get_orders():
    try:
        res = Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat())
        print(res.payload)  # json data
    except SellingApiException as ex:
        print(ex)


def test_get_order_items():
    print(Orders().get_order_items('33').payload)


def test_get_order():
    print(Orders().get_order('114-8291421-3654623').payload)
