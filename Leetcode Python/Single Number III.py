class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        z=len(nums)
        y=[0,0]
        for i in nums:
            if d.get(i)==None:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for i in d:
            if d[i]==1:
                y[c]=i
                c+=1
        return y
            
                
        