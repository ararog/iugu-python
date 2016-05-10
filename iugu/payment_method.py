

class PaymentMethod(object):

    @staticmethod
    def url(object):
        if object["customer_id"] is None:
            raise IuguException("Missing Customer ID")
        customer_id = object["customer_id"]
        object_id = None
        if object["id"] is not None:
            object_id = object["id"]
        return self::endpointAPI(object_id, "/customers/" . object["customer_id"])

    @staticmethod
    def create(attributes):
        return self::createAPI($attributes)

    @staticmethod
    def fetch(key):
        return self::fetchAPI($key)

    def save(self):
        return self.saveAPI()

    def delete(self):
        return self.deleteAPI()

    def refresh(self):
        return self.refreshAPI()

    @staticmethod
    def search(options):
        return self::searchAPI(options)
