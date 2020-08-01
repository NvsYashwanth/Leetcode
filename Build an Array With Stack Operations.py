class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        count=1
        z=[]

        i=0
        j=0
        while(i!=len(target)):
            if target[i]!=count:
                diff=target[i]-count
                count+=diff
                z.extend(['Push','Pop']*diff)


            z.append("Push")
            i+=1
            count+=1;
        return z