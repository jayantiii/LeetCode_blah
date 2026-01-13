# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is more than p and q, go to left subtree
        #if root is less than both p and q, then we can go to right
        #if one is more an done is less than , root is the answer
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

        return

#Time Complexity = O(h)
# In a BST:
# Best case (balanced): height = O(log n)
# Worst case (skewed / chain): height = O(n)

# where h = height of the tree
# That becomes:
# O(log n) in balanced BST
# O(n) in worst-case skewed BST

        