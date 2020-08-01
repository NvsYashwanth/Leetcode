# The following inputs are for testing
brak="(()())(())(()(()))"

z=[]
c=0
for i in range(len(brak)):
	if brak[i]=="(":
		if c==0:
			z.append(i)
		c+=1
	if brak[i]==")":
		c=c-1
	if c==0:
		z.append(i)
		
# The following is for debugging
# print(z)

i=0
q=[]
bra=list(brak)
# print(bra)
for i in range(len(z)-1):
	q.extend(bra[z[i]+1:z[i+1]])
print("".join(q))




# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         z=[]
#         c=0
#         for i in range(len(S)):
#             if S[i]=="(":
#                 if c==0:
#                     z.append(i)
#                 c+=1
#             if S[i]==")":
#                 c=c-1
#             if c==0:
#                 z.append(i)

#         q=[]
#         brl=list(S)
#         for i in range(len(z)-1):
#             q.extend(brl[z[i]+1:z[i+1]])
#         return("".join(q))