from api_child_resource import APIChildResource
from api_resource import APIResource
from payment_method import PaymentMethod

class Customer(APIResource):

    def __init__(self):
        self.identifier = None
        self.default_payment_method_id = None

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

    def payment_methods(self):
        return APIChildResource({"customer_id": self.identifier}, "Iugu_PaymentMethod")

    def invoices(self):
        return APIChildResource({"customer_id": self.identifier}, "Iugu_Invoice")

    def default_payment_method(self):
        if self.identifier is None:
            return False
        if self.default_payment_method_id is None:
            return False
        return PaymentMethod.fetch({"customer_id": self.identifier, "id": self.default_payment_method_id})
