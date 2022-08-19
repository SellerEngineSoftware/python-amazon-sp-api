from typing import Dict
import copy

class ItemOffersRequest:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #itemoffersrequest """
    # uri: str
    # method: str
    # MarketplaceId: str
    # ItemCondition: str = None
    # CustomerType: str = None
    # headers: Dict = None

    def __init__(self, uri, method, MarketplaceId, ItemCondition=None, CustomerType=None, headers=None):
        self.uri = uri
        self.method = method
        self.MarketplaceId = MarketplaceId
        self.ItemCondition = ItemCondition
        self.CustomerType = CustomerType
        self.headers = headers

    def to_dict(self):
        return {
            'uri': self.uri,
            'method': self.method,
            'MarketplaceId': self.MarketplaceId,
            'ItemCondition': self.ItemCondition,
            'CustomerType': self.CustomerType,
            'headers': copy.deepcopy(self.headers)
        }


class GetItemOffersBatchRequest:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #getitemoffersbatchrequest """
    # requests: Optional[List[Union[ItemOffersRequest, Dict]]] = None

    def __init__(self, requests=None):
        self.requests = self.parse_requests(requests)

    def to_dict(self):
        return {
            'requests': [request.to_dict() for request in self.requests]
        }

    @staticmethod
    def parse_requests(requests): # -> List[ItemOffersRequest]:
        parsed_requestes = []

        for request in requests:
            if isinstance(request, Dict):
                request = ItemOffersRequest(**request)

            if not isinstance(request, ItemOffersRequest):
                raise TypeError

            parsed_requestes.append(request)

        return parsed_requestes

