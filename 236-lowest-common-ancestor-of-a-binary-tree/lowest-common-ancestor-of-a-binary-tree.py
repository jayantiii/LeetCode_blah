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
            if node == p or node == q: #Understand
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

# At a given node:
# left is None and right is None
# → this whole subtree has no p or q.
# left is not None and right is None (or vice versa)
# → this subtree has at least one of (p, q) or already an LCA.
# left is not None and right is not None
# → this node is the lowest node where both sides contain something → LCA.

# ---------------- Example where p is an ancestor of q ----------------
#
# Build this tree:
#
#         3
#        / \
#       5   1
#          / \
#         0   8
#

# Let:
#   p = node 1  (parent)
#   q = node 8  (child in its subtree)

# ---- What happens conceptually in dfs(root): ----
#
# dfs(3):
#   node = 3, not p (1) or q (8)
#   -> left  = dfs(5)
#
#   dfs(5):
#       node = 5, not p or q
#       left = dfs(None)  -> None
#       right = dfs(None) -> None
#       left and right both None -> return None
#   so left = None for node 3
#
#   -> right = dfs(1)
#
#   dfs(1):
#       node == p  (since p is node 1)
#       -> return node 1 immediately
#       (we do NOT need to go down to children 0 and 8 to be correct)
#
#   so right = 1 for node 3
#
# back at dfs(3):
#   left  = None
#   right = 1
#   "if left and right" is False
#   -> return left or right -> return 1
#
# Final answer: node with value 1

#if p is in the tree and q is not in the tree, the function will still return p.
#But the problem guarantees both p and q are in the tree, so this “bad” scenario is outside the problem’s contract. Under the official constraints, it’s fine.