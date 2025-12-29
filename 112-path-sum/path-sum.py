# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return targetSum == current_sum

            left = pathsum(node.left, current_sum)
            right =  pathsum(node.right, current_sum)
            return left or right
            
        return pathsum(root,0)

#----------Mistake when i tried--------------
# The problem is that your current pathsum function sums all nodes in the subtree, not individual root-to-leaf paths. This won’t correctly solve the problem. You need to check each path from root to leaf separately.

        
        