# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        NEED, CAM, OK = 0, 1, 2
        camcount = 0
        def postorder(node):
            nonlocal camcount
            if not node:
                return OK
            left = postorder(node.left)
            right = postorder(node.right)
            
            #If child need, then place the cam on node
            if left == NEED or right == NEED:
                camcount+=1
                return CAM

            # If any child has a camera, this node is covered.
            if left == CAM or right == CAM:
                return OK
            
            # Otherwise, this node is not covered and needs its parent to cover it.
            return NEED

        #Because the root has no parent, so if it ends up uncovered (NEED), 
        #there’s nobody above it who can cover it. The only fix is to place a camera at the root.
        if postorder(root) == NEED:
            camcount += 1

        return camcount


#  a node is the cheapest “meeting point” to cover its children + itself + parent, so if a child is uncovered, placing the camera at the parent is always optimal compared to placing it lower.
# Time: O(n) (each node once). Space: O(h) recursion stack (tree height).

# Use a post-order DFS with 3 states. The greedy trick: only place a camera when a child is “uncovered” (needs coverage). That forces cameras to sit as high as possible while still fixing uncovered nodes.
# State definitions returned by dfs(node):

# NEED = 0 : this node is not covered by any camera (so its parent must cover it)
# CAM = 1 : this node has a camera
# OK = 2 : this node is covered (by a child’s camera), but has no camera

# Rules (post-order, after processing children):
# If any child is NEED → put camera here → return CAM
# Else if any child is CAM → this node is covered → return OK
# Else (both children are OK or null) → this node becomes uncovered → return NEED
# Finally, after DFS, if the root is NEED, add one more camera at the root.

##---- Inutition------------------------------------------------
# 1) What are the only situations a node can be in?
# After you’ve finished processing its children, a node is either:
# Uncovered (nobody below covered it) → it needs its parent to cover it
# Has a camera → it covers parent/self/children
# Covered but no camera (a child camera covers it)
# That’s it. Those become the 3 DFS return states: NEED, CAM, OK.

# 2) The greedy “aha”: cameras should be placed as high as possible, but only when forced
# Suppose a child is uncovered. You have two ways to fix that child:
# put a camera on the child, or put a camera on the parent.
# A camera on the parent covers more: it covers the child and the parent and potentially the sibling.
# So if a child is uncovered, placing the camera at the parent is never worse and often strictly better.
# That’s the core greedy move: “If any child needs coverage, put camera here.”

# 3) Why postorder?
# Because whether a child is uncovered / has camera / covered is only known after you solve that subtree. So:
# Solve left subtree
# Solve right subtree
# Decide what to do at current node
        