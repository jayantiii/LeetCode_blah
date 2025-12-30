# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a,b = headA, headB
        while a is not b:
            if a is None:
                a = headB
            else:
                a = a.next 

            if b is None:
                b = headA
            else:
                b = b.next
        return a


#Make both pointers traverse the same length , then will be synced and first node they meet is the intersection
# a--->None  -->b---> intersectionnode
# b--->none-->a----> intersection node
        