
class Solution:
    def productExceptSelf(self, nums):
        ans=[]
        r=[1]*len(nums)
        ans=[1]*len(nums)

        
        for i in range(1,len(nums)):
            ans[i]*=ans[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            r[i]*=r[i+1]*nums[i+1]
            ans[i]*=r[i]

        return ans