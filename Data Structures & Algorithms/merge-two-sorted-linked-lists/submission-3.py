# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2

        if list1.val <= list2.val:
            head = list1
            curr1 = list1
            curr2 = list2
        else:
            head = list2
            curr1 = list2
            curr2 = list1

        while curr1 and curr2:
            if curr1.next and curr2.val < curr1.next.val:
                nxt2 = curr2.next

                curr2.next = curr1.next
                curr1.next = curr2

                curr2 = nxt2
                curr1 = curr1.next
            elif not curr1.next:
                curr1.next = curr2
                break
            else:
                curr1 = curr1.next

        return head


