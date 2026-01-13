# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        if not root:
            return True
        return mirror(root.left, root.right)



#WRONG, Your logic is checking “same-shape” subtrees, not mirror subtrees.
        # if not root:
        #     return True
        # if root.left and root.right and root.left.val == root.right.val:
        #     return self.isSymmetric(root.left) and self.isSymmetric(root.right)

        # return False



        