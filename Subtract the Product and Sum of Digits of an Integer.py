class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        while(n!=0):
            a=n%10
            p*=a
            s+=a
            n=n//10
        return p-s
