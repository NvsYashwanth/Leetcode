class Solution:
    def findKthPositive(self, arr,k):
        check=1
        miss=[]
        m=0

        for i in range(len(arr)):
            if m<=k:
                if check!=arr[i]:
                    m+=arr[i]-check
                    miss+=list(range(check,arr[i]))
                check=arr[i]+1
        
        if m==0:
            return arr[-1]+k

        if k>=arr[-1] or k>len(miss):
            return arr[-1]+k-m
        
        if k<=len(miss):
            return miss[k-1]
        
