class Solution:
    def sortString(self, s: str) -> str:
        book={}
        for i in s:
            if book.get(i)==None:
                book[i]=1
            else:
                book[i]+=1

        res=""

        asc=sorted(set(s))
        al=len(asc)

        alpha=0
        i=0
        state="min"
        z=len(s)

        while(alpha!=z):

            if state=="min":
                if book.get(asc[i])!=None:
                    res+=asc[i]
                    alpha+=1
                    book[asc[i]]-=1

                    if book[asc[i]]==0:
                        del book[asc[i]]
                i+=1

                if i==al: 
                    state="max"
                    i-=1

            else:
                if book.get(asc[i])!=None:
                    res+=asc[i]
                    alpha+=1
                    book[asc[i]]-=1

                    if book[asc[i]]==0:
                        del book[asc[i]]
                i-=1

                if i==-1: 
                    state="min"
                    i+=1
        return res
