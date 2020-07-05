class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        z=2*n
        y=[]
        for i in range(0,n):
            y.extend([nums[i],nums[i+n]])
        return y

            
            