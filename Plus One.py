# The following inputs are for testing
# digits=[1,2,3]
digits=[4,3,2,1]

sd=[]
for i in digits:
	sd.append(str(i))

# The following is for debugging
# print(sd)

num=str(int("".join(sd))+1)

# The following is for debugging
# print(num)

sd.clear()
for i in range(len(num)):
	sd.append(int(num[i]))

print(sd)

# ------------------------------------------------------------------------

# Final code as in leetcode

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         sd=[]
#         for i in digits:
#             sd.append(str(i))
            
#         num=str(int("".join(sd))+1)
        
#         sd.clear()
#         for i in range(len(num)):
#             sd.append(int(num[i]))

#         return(sd)