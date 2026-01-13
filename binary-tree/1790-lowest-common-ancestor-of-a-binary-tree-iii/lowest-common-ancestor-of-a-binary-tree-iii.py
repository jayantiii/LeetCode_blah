"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #No root is given

        pathp = set()
        pnode = p
        while pnode:
            pathp.add(pnode)
            pnode = pnode.parent

        #Traverse q to parent
        qnode = q
        while qnode:
            if qnode in pathp: #walk from q upwards and stop at first hit in visited
                return qnode
            qnode = qnode.parent           
                


# Yes: there are multiple common ancestors in general.
# But: the algorithm is designed to return the first one seen while walking up from q, which is unique and is the LCA.

        



#you don’t have the root, but you do have parent pointers. So you solve it by going up the tree, not down.

#Store the path from p to the root.
#Traverse the path from q to the root, the first common point of the two paths is the LCA.

#Follow Up: Could you solve this using O(1) Space?
# Facebook Screening. One follow up asked was: What if one of the nodes is not in the tree?

#Mistake - implementation with DFS approach and realized when 99% done that there's no root specified,
# you don’t have the root, but you do have parent pointers. So you solve it by going up the tree, not down.