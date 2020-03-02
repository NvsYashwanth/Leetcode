# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        z={}
        x={}
        ind=0
        loc=0
        state=0
        curr=head
        if head:
            while(True):
                if state==0:
                    z[ind]=curr
                    if curr.next:
                        curr=curr.next
                        ind+=1
                    else:
                        state=1
                        head=curr


                else:
                    x[loc]=head
                    if ind!=0:
                        head.next=z[ind-1]
                        head=head.next
                        loc+=1
                        ind-=1
                    else:
                        head.next=None
                        break
        else:
            return head
        return x[0]



# ------------------------------------------- ALTERNATIVE SOLUTION -------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev=None
#         nex=None
        
#         while(head):
#             nex=head.next
#             head.next=prev
#             prev=head
#             head=nex
#         return prev
        