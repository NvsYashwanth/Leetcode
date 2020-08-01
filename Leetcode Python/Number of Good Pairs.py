class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        z=len(nums)
        c=0
        for i in range(z-1):
            for j in range(i+1,z):
                if nums[i]==nums[j]:
                    
                    c+=1
        return c
                