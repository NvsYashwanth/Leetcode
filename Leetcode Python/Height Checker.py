# The following inputs are for testing
heights=[1,1,4,2,1,3]


k=sorted(heights)

# The following is for debugging
# print(k)

c=0
for i in range(len(k)):
	if k[i]!=heights[i]:
		c+=1

print(c)


# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         k=sorted(heights)
#         c=0
#         for i in range(len(k)):
#             if k[i]!=heights[i]:
#                 c+=1
#         return(c)
