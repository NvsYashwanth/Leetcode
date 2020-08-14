class Solution:
    def longestSubarray(self, nums):
        score=max_score=0
        i=j=0
        zero=0
        occz=0
        while(i<=len(nums)-2):
            if nums[i]==1:
                score+=1
                i+=1

            elif nums[i]!=1 and nums[i+1]==1:
                if zero==0:
                    score+=1
                    j=i+1
                    i+=2
                    zero=1
                    occz=1
                else:
                    max_score=max(max_score,score)
                    score=0
                    i=j
                    zero=0
            else:
                max_score=max(max_score,score)
                score=0
                i+=1
        if nums[-2]!=0 and nums[-1]==1 and occz!=0:
            score+=1
        max_score=max(max_score,score)
        
        return max_score