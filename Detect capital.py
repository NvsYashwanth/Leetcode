class Solution:
    def detectCapitalUse(self,word):
        z=len(word)
        if 65<=ord(word[0])<=90:
            c=1
            x=0
        else:
            c=0
            x=None
        for i in word[1:]:
            if 65<=ord(i)<=90:
                c+=1
                if c==1 and x!=0:
                    return False
                else:
                    x+=1
        if c==z or (c==1 and x==0) or (c==0):
            return True

