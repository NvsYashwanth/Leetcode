class Solution:
    def countLargestGroup(self, n: int) -> int:
        # d={}
        # def addDigits(num) -> int:
        #     if num == 0:
        #         return 0
        #     if num % 9 == 0:
        #         return 9
        #     return num % 9
        # for i in range(1,n+1):
        #     z=addDigits(i)
        #     if d.get(z)==None:
        #         d[z]=1
        #     else:
        #         d[z]+=1
        # x=sorted(d.values(),reverse=True)
        # prev=x[0]
        # c=1
        # for i in range(1,len(x)):
        #     if x[i]==prev:
        #         c+=1
        #         prev=x[i]
        # return(c)
    
           # Sum digits from 1 to n inclusive. 
       #The sum is the ID of the group or the key of the dict, and the value is how many times that ID occurs 
        dic = {}        
        for i in range(1,n+1):
            sum_of_digits = sum(int(digit) for digit in str(i))            
            if dic.get(sum_of_digits):
                dic[sum_of_digits] = dic.get(sum_of_digits) + 1
            else:
                dic[sum_of_digits] = 1

        #Find the highest/max frequency among the groups
        max_members_count = max(dic.values())

        #Count how many groups have the such max frequency
        groups_count = 0
        for i in dic.values():
            if i == max_members_count:
                groups_count += 1  

        return groups_count