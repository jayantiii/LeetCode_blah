# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root): #returns height
            if not root:
                return  0

            leftheight =  dfs(root.left)
            rightheight = dfs(root.right)
            
            self.res = max(self.res,leftheight+rightheight )

            return 1+ max(leftheight,rightheight) #return that node height!

        dfs(root)
        return self.res


#--------------Difference between style A and B---------------------

# Style A:
#   leftheight  = 1 + dfs(left)
#   rightheight = 1 + dfs(right)
#   return max(leftheight, rightheight)

# Meaning: leftheight/rightheight count "nodes from CURRENT node down"
# (because you added the +1 before returning)

# Style B:
#   leftheight  = dfs(left)
#   rightheight = dfs(right)
#   return 1 + max(leftheight, rightheight)

# Meaning: leftheight/rightheight count "nodes from CHILD down"
# and you add the +1 only once when returning to parent

# Both compute the same height; they just place the "+1" in a different line.
# (Diameter formula changes accordingly: Style A needs -2 to convert nodes->edges, Style B doesn't.)



