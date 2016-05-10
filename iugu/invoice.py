

class Invoice(object):

    @staticmethod
    def create(attributes):
        return self::createAPI(attributes)

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

    def customer(self):
        if (self.customer_id is None)
            return false
        return Iugu_Customer::fetch(self.customer_id)

    def cancel(self):
        if (self.is_new())
            return False
        try:
            response = self::API().request("PUT", static::url(self) . "/cancel")
            if response.errors is not None:
                raise IuguRequestException(response.errors)
            new_object = self::createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        except e:
            return False

        return True

    def refund(self):
        if self.is_new():
            return False
        try:
            response = self::API().request("POST", static::url(self) . "/refund")
            if response.errors is not None:
                raise IuguRequestException(response.errors)
            new_object = self::createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
        raise e:
            return False

        return True
