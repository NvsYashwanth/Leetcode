class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        z=len(s)
        s_total=0
        t_total=0

        for i in range(z):
            s_total+=ord(s[i])
            t_total+=ord(t[i])
        t_total+=ord(t[z])
        return chr(t_total-s_total)
            