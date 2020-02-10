# The following inputs are for testing
s = "RLRRLLRLRL"
# s = "RLLLLRRRLR"
# s = "LLLLRRRR"

c=0
n=0
for i in range(len(s)):
    if s[i]=="L":
        c+=1
    elif s[i]=="R":
        c-=1
    if i!=0 and c==0:
        n+=1
print(n)


# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         c=0
#         n=0
#         for i in range(len(s)):
#             if s[i]=="L":
#                 c+=1
#             elif s[i]=="R":
#                 c-=1
#             if i!=0 and c==0:
#                 n+=1
#         return(n)