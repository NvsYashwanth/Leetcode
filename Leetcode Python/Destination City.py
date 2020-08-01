class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d=dict(paths)
        x=paths[0][0]
        while(True):
            if d.get(x)!=None:
                x=d[x]
            else:
                return x