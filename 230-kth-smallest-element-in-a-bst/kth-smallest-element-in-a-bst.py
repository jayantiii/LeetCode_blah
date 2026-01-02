# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # see how to strcture the function each line, imp 
        def inorder(node):
            nonlocal k
            if not node:
                return None #less than k nodes

            left = inorder(node.left)

            if left is not None:
                return left  #if the answer is found in the left subtree, dont ovewrite or decrease k
        
            k-=1  #this here
            if k == 0:
                return node.val
                
            right = inorder(node.right)
                
            return right
        #If not found in left and not current, then the answer (if it exists) must be in the right subtree.
        return inorder(root)

# Time: O(h+k) 
# You go down to the leftmost path: O(h)
# Then you “visit” nodes in sorted order until the k-th: O(k)     

# Get Inorder of BST and then return k-1 index value.
# InOrder traversal of BST is ascending order list. So, return k-1th element.

        # arr = []
        # def inorder(node):
        #     if not node: return
        #     inorder(node.left)
        #     arr.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return arr[k-1]

# ---------Follow up---------------------------------------------:
# --What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# O(h)
# Augment the BST so each node stores subtree size:
# size(node) = 1 + size(left) + size(right)
# On every insert/delete, update sizes along the path to the root.
# Then kthSmallest becomes a guided walk:
# At node:
# L = size(left)
# if k <= L: go left
# elif k == L+1: return node
# else: k -= L+1, go right

#--If it’s not a BST (just any binary tree)? then can use a heap i think

