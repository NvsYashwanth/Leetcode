class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        a=int((len(arr)*0.25)+1)
        
        i=0
        if len(arr)!=1:
            while(i!=len(arr)):
                if sum(arr[i:i+a])==arr[i]*(a):
                    return arr[i]
                i+=1
                    
        return arr[i]