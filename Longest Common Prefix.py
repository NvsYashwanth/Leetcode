class Solution:
    def longestCommonPrefix(self, strs):
        
        if strs==[] or strs==[""]:
            return ""
        elif len(strs)==1:
            return strs[0]


        min_len=len(strs[0])

        for k in strs[1:]:
            min_len = min(min_len,len(k))
            

        i=0
        j=0
        c=0
        while(j!=min_len):
            if strs[i][j]==strs[i+1][j]:
                i+=1
                if i==len(strs)-1:
                    c+=1
                    i=0
                    j+=1
            else:
                break
        if c==0:
            return ""
        return strs[0][:c]