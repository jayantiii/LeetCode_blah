# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

#Iterative
#    cur = root
#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left

#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right

#         return res

# #Dfs
#         def dfs(node):
#             if not node:
#                 return []
#             return dfs(node.left) + [node.val] + dfs(node.right)

#         return dfs(root)


        