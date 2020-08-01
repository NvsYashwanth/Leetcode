class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B=[]
        z=[]

        i=0
        j=0
        while(i!=len(A[0])):
            z.append(A[j][i])
            j+=1
            if j==len(A):
                B.append(z)
                z=[]
                j=0
                i+=1
        return B