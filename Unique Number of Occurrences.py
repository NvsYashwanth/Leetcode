# The following inputs are for testing
# arr=[1,2]
# arr = [-5,-6,2,6,-5,-7,5]
arr = [1,2,2,1,1,3]

# The following inputs are for testing
# print("Given array is : arr----> {}".format(arr))

h=list(set(arr))

# The following inputs are for testing
# print("distinct nums are : h----> {}".format(h))

z=[]
for j in range(len(h)):
	z.append(arr.count(h[j]))

# The following is for debugging
# print("Counts of distinct nums are : z----> {}".format(z))

zset=set(z)

# The following is for debugging
# print("Set of list z is : zset----> {}".format(zset))

if len(zset)!=len(z):
	print(False)
else:
	print(True)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         h=list(set(arr))
#         z=[]
#         for j in range(len(h)):
#             z.append(arr.count(h[j]))

#         zset=set(z)
        
#         if len(zset)!=len(z):
#             return(False)
#         else:
#             return(True)