# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fast=head
        slow=head
        
        if head==None or head.next==None or head.next.next==None:
            return False
        else:
            while(fast.next!=None and fast!=None and fast.next.next!=None):
                fast=fast.next.next
                slow=slow.next

                if fast==slow:
                    return True
            return False
        