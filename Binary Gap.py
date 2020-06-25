class Solution:
    def binaryGap(self, N: int) -> int:
        s=bin(N)[2:]
        dis=0
        i=0

        prev="no"

        while(i!=len(s)):
            if s[i]=='1':
                if prev=="no" or prev=="y":
                    x=i
                    i+=1
                    prev="x"
                else:
                    y=i
                    dis=max(dis,y-x)
                    x=y
                    prev="y"
            else:
                i+=1
        return dis
    
