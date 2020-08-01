# ------------------------------------------------------------------------

# Final code as in leetcode

#  class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         arr=[]
#         for i in range(left,right+1):
#             f=0
#             k=i
#             while k>0:
#                 d=k%10
#                 if d==0 or i%d!=0:
#                     f=1
#                     break
#                 k=k//10
#             if f==0:
#                 arr.append(i)
#         return arr

        