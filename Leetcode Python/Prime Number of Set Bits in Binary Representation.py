class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = [2,3,5,7,11,13,17,19,23,29,31]
        res = 0
        for n in range(L,R+1):
            if bin(n)[2:].count('1') in prime:
                res += 1
        return res