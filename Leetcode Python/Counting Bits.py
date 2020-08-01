class Solution:
    def countBits(self, num: int) -> List[int]:
        z=[0]*(num+1)
        for i in range(1,num+1):
            z[i] = z[i >> 1] + (1 if i & 1 == 1 else 0)
        return z