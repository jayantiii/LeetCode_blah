# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
# use fast slow pointers, when fast pointer reaches end, slow is mid
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

#while fast and fast.next:
# This cleanly handles both odd and even lengths:
# For odd length → fast ends at last node.
# For even length → fast ends at None.




        