# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                nxt1 = list1.next
                node.next = list1
                node = node.next
                list1 = nxt1
            else:
                nxt2 = list2.next
                node.next = list2
                node = node.next
                list2 = nxt2

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next