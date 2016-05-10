

class APIResource:

    private static _apiRequester = null;

    @staticmethod
    def convertClassToObjectType():
        object_type = str_replace("Iugu_", "", get_called_class())
        object_type = strtolower(preg_replace('/(?<=\\w)([A-Z])/', '_\\1', object_type))
        return mb_strtolower(object_type, "UTF-8")

    @staticmethod
    def objectBaseURI():
        object_type = self::convertClassToObjectType()
        switch(object_type) {
          // Add Exceptions as needed
          case 'charge':
            return object_type;
          case 'payment_token':
            return object_type;
          default:
           return object_type . 's';
        }

    @staticmethod
    def API():
        if APIResource::_apiRequester is None:
            APIResource::_apiRequester = Iugu_APIRequest()
        return APIResource::_apiRequester


    @staticmethod
    def endpointAPI(object=None, uri_path=""):
        path = ""
        if (is_string(object))
            path  = "/" . object
        else if (is_object(object) && (isset(object["id"])) )
            path = "/" . object["id"]
        return Iugu::getBaseURI() . uri_path . "/" . self::objectBaseURI() . path


    @staticmethod
    def url(object=None):
        return self::endpointAPI( object )

    @staticmethod
    def _createFromResponse(response):
        return Iugu_Factory::createFromResponse(self::convertClassToObjectType(), response)


    @staticmethod
    def _createAPI(attributes=[]):
        response = self::createFromResponse(self::API().request("POST", static::url(attributes), attributes))
        for attr => value in attributes:
            response[attr] = value
        return response

    @staticmethod
    def _deleteAPI():
        if self["id"] is None:
            return False
        try:
            response = self::API().request("DELETE", static::url(self))
            if response.errors is not None:
                raise IuguException()
        except e:
            return False
        return True

    @staticmethod
    def _searchAPI(options=Array()):
        try:
            response = self::API().request("GET", static::url(options), options)
            return self::createFromResponse(response)
        except e:

        return []

    @staticmethod
    def _fetchAPI(key):
        try:
            response = static::API().request("GET",static::url(key))
            return self::createFromResponse(response)
        except e:
            raise IuguObjectNotFound(self::convertClassToObjectType(get_called_class()) . ":" . " not found")

    def _refreshAPI():
        if self.is_new():
            return False
        try:
            response = self::API().request("GET", static::url(self))
            if response.errors is not None:
                raise IuguObjectNotFound()
            new_object = self::createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        except e:
            return False
        return True

    def _saveAPI():
        try:
            response = self::API().request(self.is_new() ? "POST" : "PUT", static::url(self), self.modifiedAttributes())
            new_object = self::createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
            if response.errors is not None:
                raise IuguException()
        except e:
            return False
        return True
