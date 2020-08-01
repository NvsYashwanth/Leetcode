class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=[]
        j=0
        for i in range(len(s)):
            if s[i]=="#":
                res[j-2:j]=chr(int(s[i-2:i])+96)
                j-=1
            else:
                res.append(chr(int(s[i])+96))
                j+=1

        return "".join(res)
        