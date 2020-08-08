class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        z=['s']*len(s)
        for i,j in zip(s,indices):
            z[j]=i
        return "".join(z)