class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        from numpy import array
        z=[]
        i=0
        j=0
        a=array(matrix)
        while(i!=len(matrix)):
            if matrix[i][j]==min(matrix[i]):
                if matrix[i][j]==max(a[:,j]):
                    z.append(matrix[i][j])
            j+=1
            if j==len(matrix[i]):
                j=0
                i+=1
        return z
