# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Dummy is there to make “delete the head” look like every other delete.
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        #Idea delay fast pointer by n
        while n > 0:
            fast = fast.next
            n-=1

        #then move both pointers same one step pace
        while fast.next:
            slow = slow.next
            fast = fast.next

        #Remove the nth node, slow pointer is on n
        slow.next = slow.next.next

        return dummy.next
        