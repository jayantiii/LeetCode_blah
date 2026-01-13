https://www.youtube.com/watch?v=XIdigk956u0 - ans from here
​
#### Using Recursion  -- uses less memory but lil more time (confusing)
###### https://www.youtube.com/watch?v=bdWOmYL5d1g - to understand
class Solution:
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
return mergeTwoLists(l1, l2)
def mergeTwoLists(self, l1, l2):
if l1 == None: return l2
if l2 == None: return l1
if l1.val <= l2.val:
l1.next = self.mergeTwoLists(l1.next, l2)
return l1
if l1.val >= l2.val:
l2.next = self.mergeTwoLists(l1, l2.next)
return l2