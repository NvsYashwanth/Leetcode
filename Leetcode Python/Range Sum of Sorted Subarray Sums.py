class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        z=[nums[0]]
        x=1
        while(x!=n):
            for i in range(x,n):
                z.append(z[-1]+nums[i])
            z.append(nums[x])
            x+=1
        z.sort()
        return sum(z[left-1:right])