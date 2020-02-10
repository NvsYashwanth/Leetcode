# The following inputs are for testing
nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

nums1.sort()
nums2.sort()

z=[]

def bs(i,n1,n2,start,end):
    if i==len(n1):
        return z
    value=n1[i]
    if start>end:
            return bs(i+1,n1,n2,start,len(nums2)-1)
    elif value not in z:
        point=(start+end)//2
        if n2[point]==value:
            z.append(value)
            return bs(i+1,n1,n2,point+1,len(nums2)-1)
        elif n2[point]>value:
            return bs(i,n1,n2,start,point-1)
        elif n2[point]<value:
            return bs(i,n1,n2,point+1,end)
    else:
        return bs(i+1,n1,n2,start,end)

answer=bs(0,nums1,nums2,0,len(nums2)-1)

#Answer
print(answer)


# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()

#         z=[]

#         def bs(i,n1,n2,start,end):
#             if i==len(n1):
#                 return z
#             value=n1[i]
#             if start>end:
#                     return bs(i+1,n1,n2,start,len(nums2)-1)
#             elif value not in z:
#                 point=(start+end)//2
#                 if n2[point]==value:
#                     z.append(value)
#                     return bs(i+1,n1,n2,point+1,len(nums2)-1)
#                 elif n2[point]>value:
#                     return bs(i,n1,n2,start,point-1)
#                 elif n2[point]<value:
#                     return bs(i,n1,n2,point+1,end)
#             else:
#                 return bs(i+1,n1,n2,start,end)

#         answer=bs(0,nums1,nums2,0,len(nums2)-1)
#         return answer