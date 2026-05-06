# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''

        cur = l1

        while cur:
            n1 += str(cur.val)
            cur = cur.next

        cur = l2

        while cur:
            n2 += str(cur.val)
            cur = cur.next

        n1 = n1[::-1]
        n2 = n2[::-1]

        res = int(n1) + int(n2)

        res_str = str(res)[::-1]

        dummy = ListNode()
        ret = dummy

        for c in res_str:
            dummy.next = ListNode(int(c))
            dummy = dummy.next

        return ret.next

            

        