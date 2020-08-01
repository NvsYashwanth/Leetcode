# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        z={}
        length=0
        curr=head
        while(curr):
            z[length]=curr
            curr=curr.next
            length+=1
            
            
        l=length//2
            
        return z[l]
            
            
            
            
        
        