class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i=0
        alpha=1
        s=alpha
        while(i!=len(nums)):
            if (nums[i]+s)>0:
                s=nums[i]+s
                i+=1
            else:
                alpha+=1
                s=alpha
                i=0
        return alpha