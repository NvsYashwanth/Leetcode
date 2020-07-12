class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        z=len(A)
        prev=A[0]
        t=True
        s=-1
        for i in range(1,z):
            if s==-1:
                if prev>A[i]:
                    s=0
                elif prev<A[i]:
                    s=1
                else:
                    pass

            else:
                if (s==0 and A[i]>prev) or (s==1 and A[i]<prev):
                    return False
            prev=A[i]
        return True