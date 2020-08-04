class Solution:

    def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
        x=abs(x)
        res=0
        while(x):
            res=res*10 + (x%10)
            x//=10
        
        return 0 if res > pow(2, 31) else res * negFlag