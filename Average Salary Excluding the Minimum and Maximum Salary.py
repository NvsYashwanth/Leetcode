class Solution:
    def average(self, salary: List[int]) -> float:
        z=len(salary)
        salary.sort()
        return (sum(salary)-salary[0]-salary[-1])/(z-2)