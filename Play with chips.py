class Solution:
    def minCostToMoveChips(self, chips): 
        even = 0
        for x in chips:
            if x%2:
                even += 1
        return min(even, len(chips)-even) # min(even,odd)