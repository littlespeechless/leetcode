from typing import  List
import queue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return None

        lo = 0
        cur = lo
        hi = len(lists)

        while lo <= hi:
            print(f'lo = {lo}, cur = {cur}, hi = {hi}')

            if lo + 1 == hi:
                if hi == 1:
                    break
                else:
                    lists[cur] = lists[lo]
                    lo = 0
                    hi = cur + 1
                    cur = lo
                    continue
            elif lo == hi:
                if cur == 1:
                    break
                else:
                    lo = 0
                    hi = cur
                    cur = lo
                    continue

            l1 = lists[lo]
            l2 = lists[lo + 1]

            c1 = l1
            c2 = l2
            c3 = ListNode()
            head = c3

            while True:
                if c1 is None:
                    if c2 is None:
                        break
                    else:
                        c3.next = c2
                        break
                elif c2 is None:
                    c3.next = c1
                    break

                if c1.val < c2.val:
                    c3.next = c1
                    c1 = c1.next
                else:
                    c3.next = c2
                    c2 = c2.next
                c3 = c3.next

            lists[cur] = head.next
            cur += 1
            lo += 2

        return lists[0]


def convert(Input: List[List[int]]) -> List[ListNode]:
    res: List[ListNode] = []

    for lst in Input:
        if len(lst) == 0:
            res.append(None)
            continue
        head = ListNode(lst[0])
        head_bak = head
        for i in range(1, len(lst)):
            head.next = ListNode(lst[i])
            head = head.next
        res.append(head_bak)

    return res

if __name__ == '__main__':
    Input = [[1,4,5],[1,3,4],[2,6]]

    sol = Solution()
    lists = convert(Input)
    res = sol.mergeKLists(lists)
    print(res)