

class Plan(object):

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
