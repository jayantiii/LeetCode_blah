# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issub(treea,treeb):
            if not treea:
                return False

            if issame(treea,treeb):
                return True

            return issub(treea.left, treeb) or issub(treea.right,treeb)


        def issame(treea,treeb):
            if not treea and not treeb:
                return True

            if not treea or not treeb:
                return False

            if treea.val != treeb.val:
                return False

            return issame(treea.left,treeb.left) and issame(treea.right,treeb.right)

        return issub(root,subRoot)
        