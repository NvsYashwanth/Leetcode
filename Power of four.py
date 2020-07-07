class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if num < 0:
            return False
        
        binary = bin(num).replace('0b','')
        count_1 = binary.count('1')
        count_0 = binary.count('0')
        
        if count_1 == 1 and count_0 %2 == 0:
            return True
        
        return False
        