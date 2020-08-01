
# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def isBoomerang(self, points: List[List[int]]) -> bool:
#         x1=points[0][0]
#         y1=points[0][1]
        
#         x2=points[1][0]
#         y2=points[1][1]
        
#         x3=points[2][0]
#         y3=points[2][1]
        
#         a=x1-x2
#         b=x2-x3
#         c=y1-y2
#         d=y2-y3
        
#         if (a*d)-(b*c)==0:
#             return False
#         return True