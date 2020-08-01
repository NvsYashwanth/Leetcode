# The following inputs are for testing
nums = [-1,0,3,5,9,12]
target = 90

def bs(nums,target,low,high):
    if low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return bs(nums,target,low,mid-1)
        else:
            return bs(nums,target,mid+1,high)
    
    else:
        return -1

g=bs(nums,target,0,len(nums)-1)
print(g)


# ------------------------------------------------------------------------

# Final code as in leetcode   

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def bs(nums,target,low,high):
#             if low<=high:
#                 mid=(low+high)//2
#                 if nums[mid]==target:
#                     return mid
#                 elif nums[mid]>target:
#                     return bs(nums,target,low,mid-1)
#                 else:
#                     return bs(nums,target,mid+1,high)

#             else:
#                 return -1
#         g=bs(nums,target,0,len(nums)-1)
#         return g