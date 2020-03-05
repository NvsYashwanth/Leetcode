class Solution:
    def romanToInt(self, s: str) -> int:
        ri={"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i=0
        num=0

        while(i!=len(s)-1):
            if ri[s[i]]>=ri[s[i+1]]:
                num+=ri[s[i]]

            else:
                num-=ri[s[i]]

            i+=1

        num+=ri[s[i]]
        
        return num