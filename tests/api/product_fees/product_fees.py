from sp_api.api import ProductFees
from sp_api.base import Marketplaces


def test_get_fees_for_sku():
    print(ProductFees().get_product_fees_estimate_for_sku('2092', 39.32))
