#The following input is mandatory
morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

words=["zocd","gjkl","hzqk","hzgq","gjkl"]
z=[]

if len(words)<=100:
	if len(words)==0:
		print(0)
	i=0
	j=0
	while(i!=len(words)):
		z.append(morse[ord(words[i][j])-97])

		j+=1
		if j==len(words[i]):
			z.append("*")
			i+=1
			j=0
		


	z.pop()
	q="".join(z)

	# The following is for debugging
	# print(q)

	words=q.split("*")

	# The following is for debugging
	# print(words)

	b=[]
	for d in words:
		if d not in b:
			b.append(d)

	print(len(b))


# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         if len(words)<=100:
#             if len(words)==0:
#                 return 0
        
#             morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#             z=[]
#             i=0
#             j=0
#             while(i!=len(words)):
#                 z.append(morse[ord(words[i][j])-97])
#                 j+=1
#                 if j==len(words[i]):
#                     z.append("*")
#                     i+=1
#                     j=0
#             z.pop()
#             q="".join(z)
#             words=q.split("*")
#             b=[]
#             for d in words:
#                 if d not in b:
#                     b.append(d)
#             return(len(b))




