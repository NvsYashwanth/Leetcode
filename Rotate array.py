class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k <= len(nums) and k != 0:
            nums[:] = nums[-k:]+nums[:len(nums)-k]
        elif k > len(nums):
            k%=len(nums)
            if k != 0:
                nums[:] = nums[-k:]+nums[:len(nums)-k]