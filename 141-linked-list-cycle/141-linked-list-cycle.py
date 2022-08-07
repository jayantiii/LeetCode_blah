# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # look notes if dont understand
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        
     
 # One way - passes all but slow
#    while head:
#             if head.val == None:
#                 return True
#             head.val = None
#             head = head.next
#         return False
            
   
        