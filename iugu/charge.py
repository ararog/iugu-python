

class Charge(object):

    @staticmethod
    def create(attributes):
        result = self::createAPI(attributes)
        if (result.success is None && result.errors is None:
            self.success = False
        return result

    def invoice(self):
        if self.invoice_id is None:
            return False
        return Iugu_Invoice::fetch(self.invoice_id)
