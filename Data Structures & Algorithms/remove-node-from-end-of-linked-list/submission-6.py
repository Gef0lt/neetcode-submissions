# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        l = 0
        curr = head

        while curr:
            l += 1
            curr = curr.next
        k = l - n

        if k == 0:
            return head.next

        curr = head 
        for i in range(k-1):
            curr = curr.next

        curr.next = curr.next.next

        return head