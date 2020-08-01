class Solution:
    def findAnagrams(self, s,p):
        z=[]
        
        if len(s)<len(p):
            return z
        
        from collections import Counter
        window_length=len(p)
        p_counter=Counter(p)

        window = Counter(s[:window_length])
        if window==p_counter:
            z.append(0)
        for i in range(1,len(s)-window_length+1):
            window[s[i-1]]-=1
            if window[s[i-1]]==0:
                del window[s[i-1]]
            window[s[i+window_length-1]]+=1

            if window==p_counter:
                z.append(i)

        return z