class Solution:
            def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
                empty=0
                drank=0
                while(numBottles):
                    drank+=numBottles
                    empty+=numBottles
                    numBottles=empty//numExchange
                    empty=empty%numExchange
                return drank