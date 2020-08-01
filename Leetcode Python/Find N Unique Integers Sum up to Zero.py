class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=[i for i in range(-n,n,2)]

        a[-1]+=n
        
        return a