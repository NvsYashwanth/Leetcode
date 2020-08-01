# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr=[]
        while head:
            arr.append(str(head.val))
            head=head.next
        arrstr="".join(arr)
        return int(arrstr,2)
        