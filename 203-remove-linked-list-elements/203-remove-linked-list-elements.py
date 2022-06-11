# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head) # dummy node to avoid more cases like val in 1st node nly
        curr = head
        prev = dummy
        while(curr):
           
            if curr.val == val: # dont shift prev wen u delete
                prev.next = curr.next
            else:
                prev = curr
            curr =curr.next
       
        return dummy.next
                
                
        