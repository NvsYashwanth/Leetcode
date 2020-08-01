class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        a=[0]*len(queries)
        for i in A:
            if i%2==0:
                s+=i
                
        for i in range(len(queries)):
            indx=queries[i][1]
            val=queries[i][0]
            
            if val%2==0:
                if A[indx]%2==0:
                    s+=val


            else:
                if A[indx]%2==0:
                    s-=A[indx]
                   

                else:
                    s+=A[indx]+val
                
            A[indx]+=val
            a[i]=s
                
            
        return a