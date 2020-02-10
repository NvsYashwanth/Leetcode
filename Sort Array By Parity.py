# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         l=len(A)-1
#         for i in range(len(A)):
#             while (A[i]%2!=0 and l>i):
#                 A[i],A[l]=A[l],A[i]
#                 l-=1
                
#         return A
        
