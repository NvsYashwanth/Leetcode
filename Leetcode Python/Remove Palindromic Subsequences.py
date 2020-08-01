class Solution:
    def removePalindromeSub(self, s: str) -> int:
 
        if len(s)!=0 and s==s[::-1]:
            return 1
        elif len(s)==0:
            return 0
        else:
            return 2