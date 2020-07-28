# https://stackoverflow.com/questions/6385190/correctness-of-sakamotos-algorithm-to-find-the-day-of-week/6385934#6385934
# https://leetcode.com/problems/day-of-the-week/discuss/382150/Python3-Solution-With-No-Knowledge-(Without-knowing-formulas-or-week-day-of-111971-beforehand)

def unknownStartDay(day, month, year):
    def hasLeapDay(year):
        return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
    
    dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # days since 31, 12, 1970
    def daysSinceStart(day, month, year):
        numDays = 0
        for y in range(year - 1, 1970, -1):
            numDays += 365 + hasLeapDay(y)
        numDays += sum(daysInMonth[:month-1])
        numDays += day 
        if month > 2:    
            numDays += hasLeapDay(year)
        return numDays
    
    knownStart = daysSinceStart(14,9,2019)
    d = daysSinceStart(day, month, year) 
    return dayNames[ (d - knownStart) % 7]