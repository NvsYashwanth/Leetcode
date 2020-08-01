class Solution:
    def toGoatLatin(self, S: str) -> str:

        z=S.split(" ")

        for i in range(len(z)):
            if z[i][0]=="a" or  z[i][0]=="e" or  z[i][0]=="i" or  z[i][0]=="o" or  z[i][0]=="u" or z[i][0]=="A" or  z[i][0]=="E" or  z[i][0]=="I" or  z[i][0]=="O" or  z[i][0]=="U":
                z[i]+="ma"+"a"*(i+1)

            elif z[i][0]!="a" and  z[i][0]!="e" and  z[i][0]!="i" and  z[i][0]!="o" and  z[i][0]!="u" and z[i][0]!="A" and  z[i][0]!="E" and  z[i][0]!="I" and  z[i][0]!="O" and  z[i][0]!="U":
                z[i]=z[i][1:]+z[i][0]+"ma"+"a"*(i+1)

        z=" ".join(z)


        
        return z