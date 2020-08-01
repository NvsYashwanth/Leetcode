# The following inputs are for testing
nums=[3,2,2,3]
val=3


x=nums.count(val)
y=len(nums)
g=y-x
i=0
j=len(nums)-1
c=j
while(i!=j and len(nums)!=0):
	if nums[i]==val:
		nums[i],nums[j]=nums[j],nums[i]
		j-=1
	else:
		i+=1

# The following is for debugging
# print(nums)
# print(len(nums[:g]))


print(nums[:g])


# ------------------------------------------------------------------------

# Final code as in leetcode
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
        
#         i=0
#         x=nums.count(val)
#         y=len(nums)
#         g=y-x
#         j=len(nums)-1
#         c=j
#         while(i!=j and len(nums)!=0):
#             if nums[i]==val:
#                 nums[i],nums[j]=nums[j],nums[i]
#                 j-=1
#             else:
#                 i+=1

#         return len(nums[:g])