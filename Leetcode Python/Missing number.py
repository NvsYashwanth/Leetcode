class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        z=len(nums)
        return z*(z+1)//2-sum(nums)