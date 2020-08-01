# Approach 1  
class Solution:
    def addDigits(self, num: int) -> int:
        t=0
        while(num>0):
            t+=num%10
            num//=10
            if num==0 and t>9:
                num=t
                t=0
        return num

# Approach 2  - - - Constant time
# Digital Root formula

class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        elif num%9==0:
            return 9
        return num%9