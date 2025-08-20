# Last updated: 8/19/2025, 10:27:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head :
            nhead = head.next
            head.next = prev
            prev = head
            head = nhead
        
        return prev

        