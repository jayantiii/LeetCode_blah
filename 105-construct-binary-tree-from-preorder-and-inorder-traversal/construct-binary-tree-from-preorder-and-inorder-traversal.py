# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre,inn):
            if not pre:
                return 
            rootval = pre[0] #find root in pre
            rootindex = inn.index(rootval) #find index in inorder
            
            root =TreeNode(rootval)
            root.left = build(pre[1:1+rootindex],inn[:rootindex])
            root.right = build(pre[rootindex+1:],inn[rootindex+1:])

            return root

        return build(preorder,inorder)

#use preorder to find the next root
#use inorder to know what nodes go in left and right subtree from the root

#rootindex (found from inorder) is the number of nodes in the left subtree.
        