# ------------------------------------------------------------------------

# Final code as in leetcodes

# class Solution:
#     def diStringMatch(self, S: str) -> List[int]:
#         N=len(S)
#         A=[i for i in range(N+1)]
#         arr=[]
#         b=0
#         e=N
#         for i in S:
#             if i=="I":
#                 arr.append(A[b])
#                 b+=1
#             elif i=="D":
#                 arr.append(A[e])
#                 e-=1
#         arr.append(A[e])
#         return arr