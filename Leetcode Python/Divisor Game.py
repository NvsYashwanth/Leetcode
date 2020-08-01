class Solution:
    def divisorGame(self, N: int) -> bool:
        x=1

        state=0

        while(N>1):
            if N%x==0:
                N-=x
                state+=1
            else:
                x+=1

        if state%2==0:
            return(False)
        else:
            return(True)