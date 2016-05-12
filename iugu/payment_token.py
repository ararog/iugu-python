from api_resource import APIResource

class PaymentToken(APIResource):

    def __init__(self):
        pass

    @staticmethod
    def create(attributes):
        return APIResource._createAPI(attributes)
