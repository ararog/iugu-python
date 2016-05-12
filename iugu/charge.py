from api_resource import APIResource
from invoice import Invoice

class Charge(APIResource):

    def __init__(self):
        pass

    @staticmethod
    def create(attributes):
        result = APIResource._createAPI(attributes)
        if result.success is None and result.errors is None:
            Charge.success = False
        return result

    def invoice(self):
        if self.invoice_id is None:
            return False
        return Invoice.fetch(self.invoice_id)
