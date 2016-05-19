from api_request import APIRequest

class APIResource:

    _apiRequester = None

    def __init__(self):
        pass

    @staticmethod
    def convertClassToObjectType():
        object_type = str_replace("Iugu_", "", get_called_class())
        object_type = strtolower(preg_replace('/(?<=\\w)([A-Z])/', '_\\1', object_type))
        return mb_strtolower(object_type, "UTF-8")

    @staticmethod
    def objectBaseURI():
        object_type = APIResource.convertClassToObjectType()
        if object_type == 'charge':
            return object_type
        elif object_type == 'payment_token':
            return object_type
        else:
            return object_type + 's'

    @staticmethod
    def API():
        if APIResource._apiRequester is None:
            APIResource._apiRequester = APIRequest()
        return APIResource._apiRequester


    @staticmethod
    def endpointAPI(object=None, uri_path=""):
        path = ""
        if is_string(object):
            path  = "/" . object
        elif is_object(object) and isset(object["id"]):
            path = "/" . object["id"]
        return Iugu.getBaseURI() + uri_path + "/" + APIResource.objectBaseURI() + path


    @staticmethod
    def url(object=None):
        return APIResource.endpointAPI( object )

    @staticmethod
    def _createFromResponse(response):
        return Factory.createFromResponse(APIResource.convertClassToObjectType(), response)


    @staticmethod
    def _createAPI(attributes=[]):
        response = APIResource._createFromResponse(APIResource.API().request("POST", url(attributes), attributes))
        for attr, value in attributes:
            response[attr] = value
        return response

    @staticmethod
    def _deleteAPI():
        if self["id"] is None:
            return False
        try:
            response = APIResource.API().request("DELETE", url(self))
            if response.errors is not None:
                raise IuguException()
        except Exception:
            return False
        return True

    @staticmethod
    def _searchAPI(options=[]):
        try:
            response = APIResource.API().request("GET", url(options), options)
            return APIResource._createFromResponse(response)
        except Exception:
            return []

    @staticmethod
    def _fetchAPI(key):
        try:
            response = APIResource.API().request("GET", url(key))
            return APIResource._createFromResponse(response)
        except e:
            raise IuguObjectNotFound(APIResource.convertClassToObjectType(get_called_class()) + ":" + " not found")

    def _refreshAPI(self):
        if self.is_new():
            return False
        try:
            response = APIResource.API().request("GET", url(self))
            if response.errors is not None:
                raise IuguObjectNotFound()
            new_object = APIResource._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        except Exception:
            return False
        return True

    def _saveAPI(self):
        try:
            response = APIResource.API().request("POST" if self.is_new() else "PUT", url(self), self.modifiedAttributes())
            new_object = APIResource._createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
            if response.errors is not None:
                raise IuguException()
        except Exception:
            return False
        return True
