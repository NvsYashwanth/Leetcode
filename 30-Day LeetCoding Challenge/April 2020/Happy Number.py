class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        z=[]
        nex=n
        while(n!=1):
            r=nex%10
            s+=r**2
            nex=nex//10

            if nex==0:
                n=s
                s=0
                nex=n
                if n in z:
                    return False
                    
                elif n==1:
                    return True
                    break
                else:
                    z.append(n)
        return True