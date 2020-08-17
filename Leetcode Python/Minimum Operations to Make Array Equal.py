class Solution:
    def minOperations(self, n: int) -> int:
        arr=[(2*i)+1 for i in range(n)]
        
        val=n
        changes=val//2
        
        res=0
        for i in range(changes):
            res+=val-arr[i]
        

        return res
        