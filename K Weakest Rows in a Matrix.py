class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        z={}
        for i in range(len(mat)):
            z.update({i:mat[i].count(1)})

        z=[x for x in sorted(z.items(), key=lambda x: x[1])][0:k]
        c=[z[i][0] for i in range(k)]
        return c

