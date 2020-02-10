# The following inputs are for testing
points=[[3,2],[-2,2]]
# points=[[1,1],[3,4],[-1,0]]

rlen = 0
for i in range(len(points)-1):

    a=points[i][0]
    b=points[i][1]

    x=points[i+1][0]
    y=points[i+1][1]

    r1=abs(x-a)
    r2=abs(y-b)

    rlen=(r1 if r1>=r2 else r2)+rlen

print(rlen)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

#         rlen = 0
#         for i in range(len(points)-1):

#             a=points[i][0]
#             b=points[i][1]

#             x=points[i+1][0]
#             y=points[i+1][1]

#             r1=abs(x-a)
#             r2=abs(y-b)

#             rlen=(r1 if r1>=r2 else r2)+rlen

#         return(rlen)