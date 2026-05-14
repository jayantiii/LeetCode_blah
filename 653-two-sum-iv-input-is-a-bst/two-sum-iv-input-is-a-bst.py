# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #O(n),O(n)
        seen = set()
        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

#Other way use propertly of BST
# Early exit not  possible though (cant stop when found like above)
# inorder traversal = sorted array (ascending) then two sum

#Naive
# You can do a DFS/BFS, store all values in a list, then do a normal Two Sum (hash set). But this ignores BST structure.  
##

#VERY WRONG recursion - You are not propagating True back up!!!
    #   def dfs(node):
    #         if k - node.val in seen:
    #             return True
    
    #         seen.add(node.val)
    #         if node.left:
    #             return dfs(node.left)
    #         if node.right:
    #             dfs(node.right)
            
    #         return False

    #     return dfs(root)