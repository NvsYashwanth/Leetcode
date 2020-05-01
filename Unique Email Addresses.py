class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        z={}
        y={}
        x={}

        c=1

        for i in emails:
            z[c]=i.split("@")
            y[c]=z[c][0].split("+")[0]
            y[c]="".join(y[c].split("."))+"@"+z[c][1]
            if x.get(y[c])==None:
                x[y[c]]=1
            c+=1
        return len(x)