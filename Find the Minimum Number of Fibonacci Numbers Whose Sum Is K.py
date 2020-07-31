class Solution:
    def findMinFibonacciNumbers(self, k):
        if k<2:
            return k

        z=[1,1]
        x=2
        i=2
        while(x<=k):
            x=z[i-1]+z[i-2]
            z.append(x)
            i+=1
        
        c=0
        i=len(z)-1
        while(k!=0):
            if z[i]<=k:
                k-=z[i]
                c+=1
            i-=1
                
        return c
    
