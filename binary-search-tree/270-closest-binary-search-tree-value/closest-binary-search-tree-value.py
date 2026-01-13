# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mindiff = float('inf')
        value = float('inf')
        while root:
            diff = abs(target - root.val)
            if mindiff > diff or (diff == mindiff and root.val < value):
                mindiff = diff
                value = root.val

            if root.val > target: #go left
                root = root.left
            elif root.val <target:# go right
                root = root.right
            else:
                return root.val

        return value

#Edge case  Q!!
# If there are multiple answers, print the smallest. Imp
# [4,2,5,1,3]
# target = 3.5 - Answer should be 3 not 4

       