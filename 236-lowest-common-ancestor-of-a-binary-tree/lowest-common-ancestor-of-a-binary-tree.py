# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: return node  #parent is the LCA
            return left or right #Both p,q are in either left or either right

        return dfs(root)



        




# Key idea:
# At each node:
# Recurse left → left
# Recurse right → right
# Then:
# If left and right are both non-None, current node is the LCA.
# If only one is non-None, bubble that upwards.
# If both None, return None.

# And remember the definition: a node can be the LCA of itself and a descendant