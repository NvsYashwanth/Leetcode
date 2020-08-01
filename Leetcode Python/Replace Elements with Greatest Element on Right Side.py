class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for _ in range(len(arr)-1):
            arr[_]=max(arr[_+1:])
        arr[-1]=-1
        return arr