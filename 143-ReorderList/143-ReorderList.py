# Last updated: 8/27/2025, 11:05:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        second = slow.next #first node of second list
        first = head       #first node of the first list

        slow.next = None   #tail of the first list and tail of the second list is alreay none

        prev = None        #to make second list reverse order we need a previous node with none
        
        while second :
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        second = prev

        while second :
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        
        