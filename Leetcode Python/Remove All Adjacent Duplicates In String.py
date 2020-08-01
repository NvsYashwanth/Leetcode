class Solution:
    def removeDuplicates(self, S: str) -> str:
        S=list(S)
        i=0
        while(i!=len(S)-1):
            if i==0 and S[i]==S[i+1]:
                del S[i]
                del S[i]
                if S==[]:
                    return ""


            elif i!=0 and S[i]==S[i+1]:
                del S[i]
                del S[i]
                if S==[]:
                    return ""
                i-=1

            else:
                i+=1
                if i==len(S)-1:
                    break
        return "".join(S)