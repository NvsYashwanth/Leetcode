# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr=ListNode(None)
        d=curr

        while(head):
            if head.val!=val:
                curr.next=head
                curr=curr.next
            
            if head.val==val and head.next==None:
                curr.next=None
                
            head=head.next

        return d.next
                
        