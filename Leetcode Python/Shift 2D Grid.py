class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n=len(grid[0])
        z=[]
        i=0
        j=0
        while(i!=len(grid)):
            z.append(grid[i][j])
            j+=1
            if j==n:
                j=0
                i+=1

        c=0
        for c in range(k):
            alpha=z[-1]
            del z[-1]
            z.insert(0,alpha)

        grid=[]
        for j in range(0,len(z),n):
            grid.append(z[j:j+n])
            
        return grid   

