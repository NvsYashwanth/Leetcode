#The following inputs are for testing
s = "abhjsweuuabcdefghijklmnobabcdefghijklmnopqrstuvwxyzbb"
# s="abababab"
# s="anviaj"


maxlen=0
c=0
z=[]
i=0
while(i!=len(s)):
	if s[i] not in z:
		z.append(s[i])
		maxlen=max(maxlen,len(z))
		i+=1

	elif s[i] in z:
		siat=z.index(s[i])

		# following line for error debugging
		# print(siat,z,s[i],len(z)) 

		z=z[siat+1:]
		z.extend(s[i])
		maxlen=max(maxlen,len(z))
		i+=1
print(maxlen)


# -------------------------------------------------------------------------------

# Final code as in Leetcode
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        c=0
        z=[]
        i=0
        while(i!=len(s)):
            if s[i] not in z:
                z.append(s[i])
                maxlen=max(maxlen,len(z))
                i+=1

            elif s[i] in z:
                siat=z.index(s[i])
                del z[:siat+1]
                z.extend(s[i])
                maxlen=max(maxlen,len(z))
                i+=1
        return(maxlen)
