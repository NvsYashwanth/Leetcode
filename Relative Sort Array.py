# The following inputs are for testing
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

z=[]

i=0
k=False
while(i!=len(arr2)):
	a=arr2[i]
	if k==False:
		c=arr1.count(a)
	if c!=0:
		k=True
		z.append(a)
		arr1.remove(a)
		c-=1
	if c==0:
		k=False
		i+=1
z.extend(sorted(arr1))

print(z)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         z=[]
#         i=0
#         k=False
#         while(i!=len(arr2)):
#             a=arr2[i]
#             if k==False:
#                 c=arr1.count(a)
#             if c!=0:
#                 k=True
#                 z.append(a)
#                 arr1.remove(a)
#                 c-=1
#             if c==0:
#                 k=False
#                 i+=1
#         z.extend(sorted(arr1))
#         return(z)


