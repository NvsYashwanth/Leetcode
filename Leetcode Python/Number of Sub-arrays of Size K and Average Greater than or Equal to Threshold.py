
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        c=0
        s=0
        
        z=len(arr)
        for i in range(z-k+1):
            if i==0:
                window=arr[:k]
                s=sum(window)

            else:
                s=s-arr[i-1]+arr[i+k-1]

            if s//k>=threshold:
                c+=1
        return c