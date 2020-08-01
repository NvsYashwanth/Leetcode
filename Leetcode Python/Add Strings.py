# Approah 1

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))


# Approah 2
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        z=max(len(num1),len(num2))

        num1=num1.zfill(z)
        num2=num2.zfill(z)

        i=z-1
        carry=0
        res=0
        j=1
        while(i>-1):
            x1=ord(num1[i])-ord('0')
            x2=ord(num2[i])-ord('0')
            value=(x1+x2+carry)%10
            carry=(x1+x2+carry)//10
            res+=j*value
            j*=10
            i-=1
        if carry>0:
            res+=j*carry
        return "%s"%res