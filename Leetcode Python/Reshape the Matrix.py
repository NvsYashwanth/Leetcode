class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np

        z=[]
        i=0
        j=0

        while(i!=len(nums)):
            z.append(nums[i][j])
            j+=1
            if j==len(nums[i]):
                j=0
                i+=1

        if r*c==len(z):
            i=0
            j=0
            k=0
            nums = np.zeros((r,c),dtype=int)
            while(i!=r):
                nums[i][j]=z[k]
                k+=1
                j+=1
                if j==c:
                    j=0
                    i+=1
        else:
            return nums
            
        return nums
