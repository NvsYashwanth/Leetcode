# The following inputs are for testing
A=[4,2,5,7]

even=[]
odd=[]
for i in range(len(A)):
	if A[i]%2==0:
		even.append(A[i])
	else:
		odd.append(A[i])

j=0
A.clear()
while(j!=len(even)):
	A.extend([even[j],odd[j]])
	j+=1
	
print(A)


# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         even=[]
#         odd=[]
#         for i in range(len(A)):
#             if A[i]%2==0:
#                 even.append(A[i])
#             else:
#                 odd.append(A[i])

#         j=0
#         A.clear()
#         while(j!=len(even)):
#             A.extend([even[j],odd[j]])
#             j+=1
#         return(A)