# Last updated: 8/26/2025, 8:20:00 PM
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        h3 = list3
        
        while list1 and list2 :
            if list1.val < list2.val :
                h3.next = list1
                h3 = h3.next
                list1 = list1.next
            else :
                h3.next = list2
                h3 = h3.next
                list2 = list2.next
        
        if list1 :
            h3.next = list1
        elif list2 :
            h3.next = list2

        return list3.next
        