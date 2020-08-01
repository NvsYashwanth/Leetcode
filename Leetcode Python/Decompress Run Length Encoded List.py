nums = [1,2,3,4]
# Output: [2,4,4,4]

z=[]


for i in range(0,len(nums)-1,2):
    vals=[nums[i+1] for j in range(nums[i])]
    z.extend(vals)

print(z)