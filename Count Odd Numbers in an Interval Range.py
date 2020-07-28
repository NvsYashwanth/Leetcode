class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if low%2!=0:
            return len(range(low,high+1,2))
        return len(range(low+1,high+1,2))

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return 0 if low > high else (high - low) // 2 + 1


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 or high % 2)