class Solution:
    def maxProduct(self, words: List[str]) -> int:
        z=len(words)
        res=0
        for i in range(z-1):
            for j in range(i+1,z):
                if set(words[i]).isdisjoint(set(words[j])):
                    l=len(words[i])*len(words[j])
                    res=(l if l>res else res)
        return res