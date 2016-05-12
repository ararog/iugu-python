

class APIChildResource:

    def __init__(self, parentKeys, className):
        self._fabricator = className
        self._parentKeys = parentKeys

    def mergeParams(self, attributes):
        return array_merge( attributes, self._parentKeys)

    def configureParentKeys(self, object):
        for key, value in self._parentKeys:
            object[key] = value
        return object

    def create(self, attributes=[]):
        result = call_user_func_array(self._fabricator + '::create', array( self.mergeparams(attributes), self._parentKeys))
        if result:
            self.configureParentKeys(result)
        return result

    def search(self, options=[]):
        results = call_user_func_array(self._fabricator + '::search', Array(self.mergeParams(options), self._parentKeys ))
        if results and results.total():
            modifiedResults = result.results()
            for i in range(0,len(modifiedResults)):
                modifiedResults[i] = self.configureParentKeys(modifiedResults[i])
            results.set(modifiedResults, results.total())
        return results

    def fetch(self, key=[]):
        if is_string(key):
            key = {"id": key}
        result = call_user_func_array(self._fabricator + '::fetch', Array( self.mergeParams(key), self._parentKeys ))
        if result:
            self.configureParentKeys(result)
        return result
