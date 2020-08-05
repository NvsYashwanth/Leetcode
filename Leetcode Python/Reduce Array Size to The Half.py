class Solution:
    def minSetSize(self, arr):
        d=Counter(arr)
        x=len(arr)
        f,h=x,x//2

        c=0
        d=sorted(d.items(),key=lambda x:x[1],reverse=True)
        for i in d:
            c+=1
            f-=i[1]
            if f<=h:
                break

        return c
