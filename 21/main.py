# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # c1 = l1
        # c2 = l2
        # s = None
        # head = None
        # while c1 is not None and c2 is not None:
        #     if not s:
        #         if c1.val < c2.val:
        #             head = c1
        #             s = c1
        #             c1 = c1.next
        #         else:
        #             head = c2
        #             s = c2
        #             c2 = c2.next
        #     else:
        #         if c1.val < c2.val:
        #             s.next = c1
        #             s = s.next
        #             c1 = c1.next
        #         else:
        #             s.next = c2
        #             s = s.next
        #             c2 = c2.next
        # if not c1:
        #     if not s:
        #         return c2
        #     s.next = c2
        # else:
        #     if not s:
        #         return c1
        #     s.next = c1
        s = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return s.next
