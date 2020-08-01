class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        z=len(nums)
        for i in range(1,z):
            nums[i]=nums[i-1]+nums[i]
        return nums