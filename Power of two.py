class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        
        binary = bin(n)[2:]
        count_1 = binary.count('1')
        count_0 = binary.count('0')
        
        if count_1 == 1:
            return True
        
        return False
        