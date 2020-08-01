class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        z=len(arr)
        diff=arr[1]-arr[0]
        for i in range(1,z-1):
            if arr[i+1]-arr[i]!=diff:
                return False
        return True
            