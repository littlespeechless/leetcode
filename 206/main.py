# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def recursive(self, node, prev=None):
    #     # recursive
    #     if not node:
    #         return prev
    #     n = node.next
    #     node.next = prev
    #     return self.recursive(n, node)

    def reverseList(self, head: ListNode) -> ListNode:
        # recursive
        # return self.recursive(head)

        # one pass
        if head is None or head.next is None:
            return head
        cursor = head.next
        head.next = None
        while cursor is not None:
            prev = cursor
            cursor = cursor.next
            prev.next = head
            head = prev
        return head

