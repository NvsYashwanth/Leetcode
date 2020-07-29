class Solution:
    def isPalindrome(self, s):
        z=[]
        s=s.lower()
        for i in s.lower():
            if i.isalnum():
                z.append(i)

        return z==z[::-1]