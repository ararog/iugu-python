

class APIChildResource:

    def __init__(self, parentKeys=[], className):
        _fabricator = className
        _parentKeys = parentKeys

    def mergeParams(self, attributes ):
        return array_merge( attributes, self._parentKeys)

    def configureParentKeys(self, object):
        for _parentKeys as key => value:
            object[key] = value
        return object

    def create(self, attributes=[]):
        result = call_user_func_array(self._fabricator . '::create', array( self.mergeparams(attributes), self._parentKeys))
        if result:
            self.configureParentKeys(result)
        return result

    def search(self, options=[]):
        results = call_user_func_array(self._fabricator . '::search', Array(self.mergeParams(options), self._parentKeys ))
        if results && results.total():
            modifiedResults = result.results()
            for i in range(0,len(modifiedResults)):
                modifiedResults[i] = self.configureParentKeys(modifiedResults[i])
            results->set(modifiedResults, results.total())
        return results

    def fetch(self, key=[]):
        if is_string(key):
            key = Array( "id" => key )
        print_r(Array(self.mergeParams(key), self._parentKeys ))
        result = call_user_func_array(self._fabricator . '::fetch', Array( self.mergeParams(key), self._parentKeys ))
        if result:
            self.configureParentKeys(result)
        return result
