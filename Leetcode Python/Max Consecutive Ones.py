class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        z=len(nums)
        if z==1:
            return nums[0]
        t,c=0,0
        for i in range(z):
            if nums[i]==1:
                c+=1
            else:
                t=max(t,c)
                c=0
        t=max(t,c)
        return t