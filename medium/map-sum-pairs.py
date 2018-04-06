class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self._data[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for key in self._data:
            if key.startswith(prefix):
                total += self._data[key]
                
        return total 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)