# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        d=head
        
        while(head and head.next):
            if head.val!=head.next.val:
                head=head.next

            else:
                head.next=head.next.next
                
        return d