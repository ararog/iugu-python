from api_resource import APIResource
from customer import Customer

class Subscription(APIResource):

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

    def add_credits(self, quantity):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("PUT", url(self) + "/add_credits", {"quantity": quantity})
            if response.errors is not None:
                return False
            new_object = APIResource._createFromResponse(response)
            self.copy( new_object )
            self.resetStates()
            return new_object
        except Exception:
            return False

        return False

    def remove_credits(self, quantity):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("PUT", url(self) + "/remove_credits", {"quantity": quantity})
            if response.errors is not None:
                return False
            new_object = APIResource._createFromResponse( response )
            self.copy( new_object )
            self.resetStates()
            return new_object
        except Exception:
            return False
        return False

    def suspend(self):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("POST", url(self) + "/suspend")
            if response.errors is not None:
                return False
            new_object = APIResource._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
            return new_object
        except Exception:
            return False
        return False

    def activate(self):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("POST", url(self) + "/activate")
            if response.errors is not None:
                return False
            new_object = APIResource._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
            return new_object
        except Exception:
            return False
        return False

    def change_plan(self, identifier):
        if self.is_new():
            return False
        if identifier is None:
            return False
        try:
            response = APIResource.API().request("POST", url(self) + "/change_plan/" + identifier)
            if response.errors is not None:
                return False
        except Exception:
            return False
        return True

    def customer(self):
        if self.customer_id is None:
            return False
        return Customer.fetch(self.customer_id)
