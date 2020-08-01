class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        f=sorted(nums)
        z={}

        i=len(f)-1
        j=i
        while(i!=0):
            if f[:j][-1]!=f[i]:
                z[f[j]]=len(f[:j])
                i-=1
                j=i
            else:
                j-=1
                if j==0:
                    z[f[j]]=0
                    i-=1
                    j=i
        z[f[i]]=0
        ans=[]

        for i in nums:
            ans.append(z[i])
        return ans
        