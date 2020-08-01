
# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def peakIndexInMountainArray(self, A: List[int]) -> int:
#         def binarysearch(A,low,high):
#             if low>=high:
#                 return low
#             else:
#                 mid=(low+high)//2
#                 if A[mid-1]<A[mid]>A[mid+1]:
#                     return mid
#                 elif A[mid-1]<A[mid]<A[mid+1]:
#                     return binarysearch(A,mid+1,high)
#                 else:
#                     return binarysearch(A,low,mid-1)

#         i=binarysearch(A,0,len(A)-1)
#         return(i)
