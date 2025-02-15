# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #O(m + n), O(1)
        l1 = list1
        l2 = list2
        res = ListNode() #dummy
        tail = res
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next #This step needed, so that it moves to new added node
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return res.next # because first node is dummy node



        