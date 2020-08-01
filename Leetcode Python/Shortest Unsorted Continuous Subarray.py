class Solution:
    def findUnsortedSubarray(self, nums):
        z=sorted(nums)
        if z==nums:
            return 0
        
        else:
            for i in range(len(z)):
                if nums[i]!=z[i]:
                    l=i
                    break

            for j in range(len(z)-1,-1,-1):
                if nums[j]!=z[j]:
                    r=j
                    break

        return r-l+1