from iugu_exceptions import IuguRequestException
from api_resource import APIResource
from customer import Customer

class Invoice(APIResource):

    def __init__(self):
        self.customer_id = None

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

    def customer(self):
        if self.customer_id is None:
            return False
        return Customer.fetch(self.customer_id)

    def cancel(self):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("PUT", url(self) + "/cancel")
            if response.errors is not None:
                raise IuguRequestException(response.errors)
            new_object = APIResource.API()._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        except IuguRequestException:
            return False

        return True

    def refund(self):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("POST", url(self) + "/refund")
            if response.errors is not None:
                raise IuguRequestException(response.errors)
            new_object = APIResource.API()._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        except IuguRequestException:
            return False

        return True
