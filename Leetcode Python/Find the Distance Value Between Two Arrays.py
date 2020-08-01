class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        t=0
        a=len(arr1)
        b=len(arr2)
        for i in range(a):
            c=0
            for j in range(b):
                if abs(arr1[i]-arr2[j])>d:
                    c+=1
            if c==b:
                t+=1
            c=0
        return t