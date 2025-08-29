# Last updated: 8/28/2025, 10:15:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head :
            return None

        count = 0
        h1 = head
        while h1 :
            h1 = h1.next
            count+=1
            
        
        prev = None 
        h2 = head
        count1 = 1
        while h2 :
            if (count - n) + 1 == count1 :
                if prev == None :
                    return head.next
                prev.next = h2.next
                return head
            
            prev = h2
            h2 = h2.next
            count1 += 1
            
        