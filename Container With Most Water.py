class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=min(height[i],height[j])*(j-i)

        if j==i+1:
            return area

        else:
            if height[i]<height[j]:
                point=i
                rest=j
            else:
                point=j
                rest=i


            while(i!=j):
                if height[rest]<height[point]:
                    point,rest=rest,point

                elif height[rest]==height[point]:
                    s=min(height[point],height[rest])
                    w=abs(rest-point)
                    c_area=w*s
                    area=max(c_area,area)
                    if height[i+1]>height[j-1]:
                        point,rest=i+1,j
                    else:
                        point,rest=j-1,i

                i,j=min(point,rest),max(point,rest)

                s=min(height[point],height[rest])
                w=abs(rest-point)
                c_area=w*s
                area=max(c_area,area)

                if s==height[rest]:
                    point,rest=rest,point

                if point==j:
                    point-=1
                else:
                    point+=1
                i,j=min(point,rest),max(point,rest)
            return area