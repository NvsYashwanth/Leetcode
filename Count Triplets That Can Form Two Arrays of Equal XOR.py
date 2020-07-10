class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        z=len(arr)

        c=0

        for i in range(z-1):
            res=0
            for j in range(i,z):
                res^=arr[j]
                if res==0:
                    c+=j-i
        return c