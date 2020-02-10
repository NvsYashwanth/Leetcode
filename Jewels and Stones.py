# The following inputs are for testing	
J = "aA"
S = "aAAbbbb"
J = "z" 
S = "ZZ"

lj=list(J)
ls=list(S)
c=0
for i in range(len(ls)):
	if ls[i] in lj:
		c+=1

# The following is for debugging
# print(len(S))

print(c)

# ------------------------------------------------------------------------

# Final code as in leetcode
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#             lj=list(J)
#             ls=list(S)
#             c=0
#             for i in range(len(ls)):
#                 if ls[i] in lj:
#                     c+=1
#             return c
        
