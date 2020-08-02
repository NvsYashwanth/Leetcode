class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s=set()
        

    def add(self, key: int):
        self.s.add(key)
        

    def remove(self, key: int):
        try:
            self.s.remove(key)
        except KeyError:
            pass

    def contains(self, key: int):
        """
        Returns true if this set contains the specified element
        """
        if key in self.s:
            return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)