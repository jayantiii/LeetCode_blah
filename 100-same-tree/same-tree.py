# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val:
            left = self.isSameTree(p.left,q.left) 
            right = self.isSameTree(p.right,q.right)
            return left and right
        else:
            return False


#clean!
        # if not p and not q:
        #     return True
        
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # return False
        