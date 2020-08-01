class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        new=bin(x^y)[2:]
        return new.count('1')