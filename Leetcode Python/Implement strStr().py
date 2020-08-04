class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        z=len(needle)
        if z==0:
            return 0
        if z==1 and len(haystack)==1:
            return 0
        
        for i in range(0,len(haystack)-1):
            if haystack[i:i+z]==needle:
                return i
            
        return -1
        