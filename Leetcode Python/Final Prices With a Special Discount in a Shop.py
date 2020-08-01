class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i=0
        j=1
        z=len(prices)
        while(i<z-1):
            if prices[j]<=prices[i]:
                prices[i]-=prices[j]
                i+=1
        
                j=i+1

            elif prices[j]>=prices[i]:
                j+=1


            if j==z:
                i+=1
                j=i+1
        return(prices)
