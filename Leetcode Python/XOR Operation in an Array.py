class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        from functools import reduce
        z=[start+i*2 for i in range(0,n)]
        return reduce(lambda a,b : a^b, z)