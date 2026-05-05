# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_curr = ListNode()
        ans_head = ListNode(0, ans_curr)
        while l1 and l2:
            ans_curr.next = ListNode((l1.val + l2.val + ans_curr.val) // 10)
            ans_curr.val = (l1.val + l2.val + ans_curr.val) % 10


            l1 = l1.next
            l2 = l2.next
            ans_prev = ans_curr
            ans_curr = ans_curr.next
        while l1:
            ans_curr.next = ListNode((l1.val + ans_curr.val) // 10)
            ans_curr.val = (l1.val + ans_curr.val) % 10
            ans_prev = ans_curr
            ans_curr = ans_curr.next
            l1 = l1.next

        while l2:
            ans_curr.next = ListNode((l2.val + ans_curr.val) // 10)
            ans_curr.val = (l2.val + ans_curr.val) % 10
            ans_prev = ans_curr
            ans_curr = ans_curr.next
            l2 = l2.next
        
        if ans_curr.val == 0:
            ans_prev.next = None
        return ans_head.next
