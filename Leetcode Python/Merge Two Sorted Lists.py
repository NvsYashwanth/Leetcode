class Solution:
    def mergeTwoLists(self, N, M):
        head = curr = ListNode(0)
        while N and M:
            if N.val < M.val:
                curr.next, N = N, N.next
            else:
                curr.next, M = M, M.next
            curr = curr.next
        curr.next = N or M
        return head.next