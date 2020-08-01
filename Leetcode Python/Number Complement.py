class Solution:
    def findComplement(self, num: int) -> int:
        num=[2**i*(int(x)^1) for i,x in enumerate(bin(num)[2:][::-1])]
        
        return sum(num)