

class Customer(object):

    @staticmethod
    def create(attributes):
        return self::createAPI(attributes)

    @staticmethod
    def fetch(key):
        return self::fetchAPI(key)

    def save(self):
        return self.saveAPI()

    def delete(self):
        return self.deleteAPI()

    def refresh(self):
        return self.refreshAPI()

    @staticmethod
    def search(options):
        return self::searchAPI($options)

    def payment_methods(self):
        return APIChildResource(Array("customer_id" => self.id), "Iugu_PaymentMethod")

    def invoices(self):
        return APIChildResource(Array("customer_id" => self.id), "Iugu_Invoice")

    def default_payment_method(self):
        if self.id is None:
            return False
        if self.default_payment_method_id is None:
            return False
        return Iugu_PaymentMethod::fetch(Array("customer_id" => self.id, "id" => self.default_payment_method_id))
