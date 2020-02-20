class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        i=0
        j=0

        while(i!=len(grid)):

            if grid[i][j]<0:
                c+=1

            j+=1

            if j==len(grid[i]):
                j=0
                i+=1
        return c