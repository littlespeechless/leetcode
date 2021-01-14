# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two pointer method
        if not head.next:
            return None
        p1 = head
        p2 = head
        for i in range(n-1):
            p2 = p2.next
        # loop
        prev = None
        while p2.next is not None:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        if prev is None:
            return p1.next
        prev.next = p1.next
        return head
        # simple solution
        # fast = slow = head
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head
