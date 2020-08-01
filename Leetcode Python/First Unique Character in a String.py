class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        
        for i in range(len(s)):
            if d.get(s[i])==None:
                d[s[i]]=[1,i]
            else:
                d[s[i]][0]+=1
                
                
        for i in d:
            if d[i][0]==1:
                return d[i][1]
        return -1
        