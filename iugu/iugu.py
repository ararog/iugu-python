
class Iugu:

    VERSION = "1.0.6"
    api_key = None
    api_version = "v1"
    endpoint = "https://api.iugu.com"

    @staticmethod
    def getBaseURI():
        return endpoint . "/" . api_version

    @staticmethod
    def setApiKey(_api_key):
        api_key = _api_key

    @staticmethod
    def getApiKey():
        return api_key
