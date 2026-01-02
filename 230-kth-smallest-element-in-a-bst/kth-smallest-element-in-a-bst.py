# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            nonlocal k
            if not node:
                return None #less than k nodes

            left = inorder(node.left)
            if left is not None:        #if the answer is found in the left subtree, return it
                return left
        
            k-=1 
            if k == 0:
                return node.val
            right = inorder(node.right)
                
            return right
        #If not found in left and not current, then the answer (if it exists) must be in the right subtree.
        return inorder(root)
        




# Dummy Approach:
# Get Inorder of BST and then return k-1 index value.
# InOrder traversal of BST is ascending order list. So, return k-1th element.

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

