class Solution:
    def checkInclusion(self, s1,s2):
        
        if len(s2)<len(s1):
            return False
        
        from collections import Counter
        window_length=len(s1)
        s1_counter=Counter(s1)

        window = Counter(s2[:window_length])
        if window==s1_counter:
            return True

        for i in range(1,len(s2)-window_length+1):
            window[s2[i-1]]-=1
            if window[s2[i-1]]==0:
                del window[s2[i-1]]
            window[s2[i+window_length-1]]+=1

            if window==s1_counter:
               return True

        return False