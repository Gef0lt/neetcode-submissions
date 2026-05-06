# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        elif not list1:
            return list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        ret = list1

        while list1.next and list2:
            if list2.val <= list1.next.val:
                next2 = list2.next
                list2.next = list1.next
                list1.next = list2

                list2 = next2
            else:
                list1 = list1.next

        if list2:
            list1.next = list2
    

        return ret