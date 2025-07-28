# Last updated: 7/28/2025, 12:51:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = '', ''
        
        while l1 or l2 :
            if l1:
                n1 = n1 + str(l1.val)
                l1 = l1.next
            else:
                n1 = n1 + '0'
                
            if l2:
                n2 = n2 + str(l2.val)
                l2 = l2.next
            else:
                n2 = n2 + '0'
        
        
        n1 = int(n1[::-1])
        
        n2 = int(n2[::-1])
        
        
        
        n3 = n1 + n2
        
        
        n3 = str(n3)[::-1]
        
        l3 = ListNode()
        nn = l3
        for i in range(len(n3)):
            nn.next = ListNode(int(n3[i]))
            nn = nn.next
            
        return l3.next