class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        nums={}
        ans=-1
        if len(arr)==1:
            if arr[0]==1:
                return 1
            else:
                return -1
        else:
            for i in range(len(arr)-1):
                if nums.get(arr[i])==None:
                    nums[arr[i]]=1
                else:
                    nums[arr[i]]+=1
                if nums[arr[i]]==arr[i] and arr[i+1]!=arr[i]:
                    ans=max(ans,nums[arr[i]])

            if nums.get(arr[i+1])==None:
                    nums[arr[i+1]]=1
            else:
                nums[arr[i+1]]+=1
            if nums[arr[i]]==arr[i]:
                ans=max(ans,nums[arr[i+1]])
        return ans