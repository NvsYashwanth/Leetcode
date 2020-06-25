class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        book={}
        for i in nums:
            if book.get(i)==None:
                book[i]=1
            else:
                book[i]+=1

        for i in book:
            if book[i]==1:
                return i