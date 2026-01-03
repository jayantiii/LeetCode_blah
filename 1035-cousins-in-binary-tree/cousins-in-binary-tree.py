# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        px,py = None, None
        dx, dy = -1,-1
        def cousins(node,parent,depth):
            nonlocal px, py, dx, dy
            if not node:
                return

            if node.val == x:
                px,dx = parent, depth
            if node.val == y:
                py,dy = parent, depth
 
            if dx != -1 and dy != -1:  # both found, stop
                return
            cousins(node.left, node, depth + 1)
            cousins(node.right, node, depth + 1)

        cousins(root, None, 0)
        if px != py and dx == dy:
            return True
        else:
            return False
        
#using this is worng --> height(node) = 1 + max(height(node.left), height(node.right))
# It's "wrong" for THIS problem (cousins) because cousins does NOT ask for tree height / max depth.
# Cousins needs only:
#   1) depth of x and depth of y (distance from root),
#   2) parent of x and parent of y.
# - height(...) is correct for problems like "max depth of binary tree"
# - but irrelevant / useless for determining whether x and y are cousins

##--------------BFS WAY----------------------------------------
# def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
#         if not root:
#             return False

#         q = deque([(root, None)])  # (node, parent)

#         while q:
#             px = py = None
#             level_size = len(q)

#             for _ in range(level_size):
#                 node, parent = q.popleft()

#                 if node.val == x:
#                     px = parent
#                 elif node.val == y:
#                     py = parent

#                 if node.left:
#                     q.append((node.left, node))
#                 if node.right:
#                     q.append((node.right, node))

#             # after processing the whole level
#             if px and py:
#                 return px != py        # same level, different parents
#             if (px is None) != (py is None):
#                 return False           # found only one at this level => depths differ

#         return False
