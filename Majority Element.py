class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        y=len(nums)/2
        z={}
        for i in nums:
            if z.get(i)==None:
                z[i]=1
            else:
                z[i]+=1
            if z[i]>y:

                return i