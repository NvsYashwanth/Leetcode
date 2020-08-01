class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        s=True

        i=0
        j=0

        while(True):
          if len(matrix)==1 or len(matrix[0])==1:
            s=True
            break

          else:
            if matrix[i][j]==matrix[i+1][j+1]:
              j+=1
              if j==len(matrix[0])-1:
                i+=1
                if i==len(matrix)-1:
                  break
                j=0
            else:
              s=False
              break
        return s

