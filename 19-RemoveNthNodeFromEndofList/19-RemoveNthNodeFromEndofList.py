# Last updated: 8/28/2025, 10:33:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 :
            right = right.next
            n -= 1
        
        while right :
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        
        
        
        
        
        
        
        
        '''if not head :
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
            count1 += 1'''
            
        