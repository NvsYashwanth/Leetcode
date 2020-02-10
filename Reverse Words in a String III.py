# The following inputs are for testing
s="Let's take LeetCode contest"

p=s.split(" ")

# The following is for debugging
# print(p)

z=[]

for i in p:
	z.append(i[::-1])
print(" ".join(z))



# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         p=s.split(" ")
#         z=[]
#         for i in p:
#             z.append(i[::-1])
#         return(" ".join(z))
