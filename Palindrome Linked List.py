# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        z=[]
        while(head):
            z.append(head.val)
            head=head.next
        
        if z==z[::-1]:
            return True
        else:
            return False
            