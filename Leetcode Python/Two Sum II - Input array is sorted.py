class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        z=[]
        i=0
        j=len(numbers)-1

        while(i<=j):
            if numbers[i]+numbers[j]==target:
                z.extend([i+1,j+1])
                break
            elif numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1

            
        return z