# The following inputs are for testing
A=[5,1,5,2,5,3,5,4]
# A=[1,2,2,3]


for i in set(A):
	if A.count(i)==len(A)//2:
		ans=i

print("Answer is ---> %d"%ans)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         for i in set(A):
#             if A.count(i)==len(A)//2:
#                 return(i)

