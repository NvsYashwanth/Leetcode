class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        z=[]
        for i in nums:
            if d.get(i)==None:
                d[i]=1
            else:
                z+=i,
        return z
        