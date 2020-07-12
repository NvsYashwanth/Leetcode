class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s,2)
        c=0
        while(num!=1):
            if num%2==0:
                num//=2
            else:
                num+=1
                
            c+=1
        return c