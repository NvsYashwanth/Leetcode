class Solution:
    def numSub(self, s: str) -> int:
        s=s.split('0')
        c=0
        y=[]
        for i in range(len(s)):
            if s[i]!="":
                z=len(s[i])
                y.extend(list(range(1,z+1)))
        return(sum(y)%(10**9+7))
        