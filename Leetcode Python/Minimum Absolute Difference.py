# The following inputs are for testing
arr =  [-25,-51,-29,-23,57,-18]
if (len(arr)>=2 and len(arr)<=10**5) and (arr[-1]<=10**6 and arr[0]>=-10**6):
	arr.sort()
	
	# The following is for debugging
	# print(arr)

	g=abs(arr[1]-arr[0])
	z=[]
	
	for i in range(len(arr)-1):
		if abs(arr[i]-arr[i+1])==g:
			z.append([arr[i],arr[i+1]])
		if abs(arr[i]-arr[i+1])<g:
			g=abs(arr[i]-arr[i+1])
			z.clear()
			z.append([arr[i],arr[i+1]])

	print(z)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

#         if (len(arr)>=2 and len(arr)<=10**5) and (arr[-1]<=10**6 and arr[0]>=-10**6):
#             arr.sort()
#             # print(arr)

#             g=abs(arr[1]-arr[0])
#             z=[]

#             for i in range(len(arr)-1):
#                 if abs(arr[i]-arr[i+1])==g:
#                     z.append([arr[i],arr[i+1]])
#                 elif abs(arr[i]-arr[i+1])<g:
#                     g=abs(arr[i]-arr[i+1])
#                     z.clear()
#                     z.append([arr[i],arr[i+1]])

#             return(z)

            
                
        