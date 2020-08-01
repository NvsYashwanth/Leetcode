class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if d.get(i)==None:
                d[i]=1
            else:
                return True
        return False
            