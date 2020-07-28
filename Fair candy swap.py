class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sa=sum(A)
        sb=sum(B)
        a=set(A)
        b=set(B)
        for i in A:
            z=i+(sb-sa)//2
            if z in b:
                return [i,z]

            