

class Subscription(object):

    @staticmethod
    def create(attributes):
        return self::createAPI(attributes)

    @staticmethod
    def fetch(key):
        return self::fetchAPI(key)

    def save():
        return self.saveAPI()

    def delete():
        return self.deleteAPI()

    def refresh():
        return self.refreshAPI()

    @staticmethod
    def search(options):
        return self::searchAPI(options)

    def add_credits(self, quantity):
        if self.is_new():
            return False
        try:
            response = self::API()->request("PUT", static::url(self) . "/add_credits", Array( "quantity" => quantity ))
            if response.errors is not None:
                return False
            new_object = self::createFromResponse( response )
            self.copy( new_object )
            self.resetStates()
            return new_object
        except e:
            return False

        return False

    def remove_credits(self, quantity):
        if self.is_new():
            return False
        try:
            response = self::API().request("PUT", static::url(self) . "/remove_credits", Array( "quantity" => quantity ))
            if response.errors is not None
                return False
            new_object = self::createFromResponse( response )
            self.copy( new_object )
            self.resetStates()
            return new_object
        except e:
            return False
        return False

    def suspend(self):
        if self.is_new():
            return False
        try:
            response = self::API()->request("POST", static::url(self) . "/suspend")
            if response.errors is not None:
                return False
            new_object = self::createFromResponse(response)
            self.copy(new_object)
            self.resetStates()
            return new_object
        except e:
            return False
        return False

    def activate(self):
        if self.is_new():
            return False
        try:
            response = self::API().request("POST", static::url(self) . "/activate")
            if response.errors is not None:
                return False
            new_object = self::createFromResponse(response);
            self.copy(new_object)
            self.resetStates()
            return new_object
        raise e:
            return False
        return False

    def change_plan(self, identifier):
        if self.is_new():
            return False
        if identifier is None:
            return False
        try:
            response = self::API().request("POST", static::url(self) . "/change_plan/" . identifier)
            if response.errors is not None:
                return False
        except e:
          return False
        return True

    def customer(self):
        if self.customer_id is None:
            return False
        return Iugu_Customer::fetch(self.customer_id)
