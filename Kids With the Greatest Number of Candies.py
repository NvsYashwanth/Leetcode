class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        val=max(candies)
        z=[]
        for i in candies:
            if (i+extraCandies)>=val:
                z.append(True)
            else:
                z.append(False)
        return z