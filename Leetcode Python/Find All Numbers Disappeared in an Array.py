class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={i:0 for i in range(1,len(nums)+1)}
        for i in nums:
            d[i]+=1

        z=[i for i in d if d[i]==0]
        return z
        # return set(range(1,len(nums)+1))-set(nums)