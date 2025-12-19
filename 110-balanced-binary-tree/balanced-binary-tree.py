# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(right_height - left_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root):
            if not root:
                return 0         
            return 1 + max(self.height(root.left), self.height(root.right))

        
    # clear code
#     def isBalanced(self, root):
#         # Helper function to check height and balance
#         def height(node):
#             # If the node is empty, height is 0
#             if not node:
#                 return 0
#
#             # Get height of left subtree
#             left = height(node.left)
#             # If left subtree is unbalanced, propagate -1
#             if left == -1:
#                 return -1
#
#             # Get height of right subtree
#             right = height(node.right)
#             # If right subtree is unbalanced, propagate -1
#             if right == -1:
#                 return -1
#
#             # If height difference is more than 1, tree is unbalanced
#             if abs(left - right) > 1:
#                 return -1
#
#             # Return height of current node
#             return 1 + max(left, right)
#
#         # Tree is balanced if height does not return -1
#         return height(root) != -1
