class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        z=[]
        for i in range(len(S)):
            if 65<=ord(S[i])<=90 or 97<=ord(S[i])<=122:
                z.append(S[i])

        z=z[::-1]

        i=0
        j=0

        while(i!=len(S)):
            if 65<=ord(S[i])<=90 or 97<=ord(S[i])<=122:
                pass

            else:
                z.insert(j,S[i])
            j+=1
            i+=1
            
        z="".join(z)
        
        return z