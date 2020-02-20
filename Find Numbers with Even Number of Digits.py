class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0

        for i in range(len(nums)):

            if len(str(nums[i]))%2 == 0:
                c+=1

        return c