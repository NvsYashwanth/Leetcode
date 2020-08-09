class Solution:
    def makeGood(self, s: str) -> str:
        if s=='' or s==' ':
            return s
        z=list(s)
        i=j=0
        x=0
        while(j<len(s)-1-x):
            if abs(ord(z[j])-ord(z[j+1]))==32:
                if j!=0:
                    del z[j:j+2]
                    j-=1
                else:
                    del z[:2]
                    j=0
                x+=2
                
            else:
                j+=1
        return ''.join(z)
