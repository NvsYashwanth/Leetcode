# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         magv=0
#         magh=0
#         for i in moves:
#             if i=="U":
#                 magv+=1
                
#             elif i=="D":
#                 magv-=1
                
            
#             elif i=="R":
#                 magh+=1
                
#             elif i=="L":
#                 magh-=1
        
#         if magh==magv==0:
#             return True
        
        
#         return False