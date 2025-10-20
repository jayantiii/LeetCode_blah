# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#The reverse order is intentional and correct 
# least significant digit first, which simplifies the addition 
        dummy = ListNode() # dummy head
        head = dummy
        carry = 0
        while l1 or l2 or carry :
            l1val = l1.val if l1 else 0 # 0, like this if only carry left
            l2val = l2.val if l2 else 0
            res = l1val + l2val + carry
            new_digit = res % 10
            carry = res // 10
            head.next = ListNode(new_digit) #IMP , DONT DO  head.val = new_digit like this
            head = head.next
            l1 = l1.next if l1 else None # like this!!
            l2 = l2.next if l2 else None


        return dummy.next

      # this not needed, handle in loop
        # if carry: 
        #     head.next
        #     head.value = carry




        