class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        import numpy as np
        mat = np.zeros((n,m),dtype=int)

        i=0
        j=0
        c=0
        while(i!=len(indices)):
            if c==0:
                mat[indices[i][0]]+=1

            mat[j][indices[i][1]]+=1
            c=1
            j+=1

            if j==mat.shape[0]:
                j=0
                i+=1
                c=0
        t=0
        for i in mat:
            for j in i:
                if j%2!=0:
                    t+=1
        return t

        