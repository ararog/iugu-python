from iugu_exceptions import IuguException
from api_resource import APIResource

class PaymentMethod(APIResource):

    def __init__(self):
        pass

    @staticmethod
    def url(object):
        if object["customer_id"] is None:
            raise IuguException("Missing Customer ID")
        customer_id = object["customer_id"]
        object_id = None
        if object["id"] is not None:
            object_id = object["id"]
        return APIResource.endpointAPI(object_id, "/customers/" + object["customer_id"])

    @staticmethod
    def create(attributes):
        return APIResource._createAPI(attributes)

    @staticmethod
    def fetch(key):
        return APIResource._fetchAPI(key)

    def save(self):
        return self._saveAPI()

    def delete(self):
        return self._deleteAPI()

    def refresh(self):
        return self._refreshAPI()

    @staticmethod
    def search(options):
        return APIResource._searchAPI(options)
