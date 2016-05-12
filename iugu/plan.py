from api_resource import APIResource

class Plan(APIResource):

    def __init__(self):
        pass

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
