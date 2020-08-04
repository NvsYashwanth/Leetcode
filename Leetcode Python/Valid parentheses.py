class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        check={")":"(","}":"{","]":"["}

        for i in s:
            if d==[]:
                d+=i
            else:
                if i in check and d[-1]==check[i]:
                    d.pop()
                else:
                    d+=i

        if len(d)==0:
            return True
        return False

        