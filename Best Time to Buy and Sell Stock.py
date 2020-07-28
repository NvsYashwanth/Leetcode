class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit,min_price=0,float('inf')
        for price in prices:
            if min_price>price:
                min_price=price

            profit=price-min_price
            if max_profit<profit:
                max_profit=profit

        return max_profit