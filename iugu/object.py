class Object:

    def __init__(self, attributes=[]):
        self._attributes = []
        self._unsavedAttributes = []
        foreach (attributes as key=>value):
            self._attributes[key] = value

    def __set(self, key, value):
        self.offsetSet(key, value)

    def __isset(self, key):
        return self.offsetExists(key)

    def __unset(self, key):
        self.offsetUnset(key)

    def __get(self, key):
        return self.offsetGet(key)

    def offsetSet(self, key, value):
        self._attributes[key] = value
        self._unsavedAttributes[key] = 1

    def offsetExists(self, k):
        return array_key_exists(k, self._attributes)

    def offsetUnset(self, key):
        unset(self._attributes[key])
        unset(self._unsavedAttributes[key])

    def offsetGet(self, key):
        return array_key_exists(key, self._attributes) ? self._attributes[key] : null

    def keys(self):
        return array_keys(self._attributes)

    def modifiedAttributes(self):
        return array_intersect_key( self._attributes, self._unsavedAttributes )

    def resetStates(self):
        self._unsavedAttributes=Array()

    def is_new(self):
        return self._attributes["id"] is None

    def copy(self, object):
        foreach (object->keys() as key):
            self._attributes[key] = object[key]

    def __toString(self):
        if self._attributes["id"] is not None:
            return self._attributes["id"]
        return get_called_class()
