# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements = set()
        curr = head
        prev = None
        while(curr):
            if curr.val in elements:
                temp = curr
                curr = curr.next
                prev.next = temp.next
                
            else:
                elements.add(curr.val)
                prev = curr
                curr = curr.next
        print(elements)  
        return head
                
          
            
        