class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        p=[x for x in range(1,m+1)]
        z=[]
        for i in range(len(queries)):
            loc=p.index(queries[i])
            z.append(loc)
            p=[p[loc]]+p[:loc]+p[loc+1:]

        return z