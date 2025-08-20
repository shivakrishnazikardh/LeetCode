# Last updated: 8/19/2025, 10:36:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prev = None
        
        #while head :
        #    nhead = head.next
        #    head.next = prev
        #    prev = head
        #    head = nhead
        
        #return prev

        if not head :
            return None

        nhead = head 
        if head.next :
            nhead = self.reverseList(head.next)
            fhead = head.next
            fhead.next = head

        head.next = None
        return nhead
        

        