class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        y=len(startTime)
        for i in range(y):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                c+=1
        return c
        