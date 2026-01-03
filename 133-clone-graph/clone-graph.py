"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = set()
        clone = {} # original_node -> cloned_node
        def dfs(n): #return cloned node
            if not n:
                return

            # already cloned => reuse (handles cycles + shared nodes)
            if n in clone:
                return clone[n] #just return, dont continue

            # create clone FIRST, store it, THEN expand neighbors
            newnode = Node()
            newnode.val = n.val
            newnode.neighbors = []
            clone[n] = newnode #Imp - store early ( before the loop): or infinite recursion
            for nei in n.neighbors:
                clonenei = dfs(nei)
                newnode.neighbors.append(clonenei)

            return newnode
            

        return dfs(node)

#Deep copy = you return a new graph with brand-new Node objects, not reusing any original nodes. The clone must preserve the same connections (neighbors), but modifying the clone must not affect the original.

# The first time you encounter an original node, you create its clone and store it in the hashmap.
# Every later time you encounter that same original node (via another edge), you reuse the existing clone from the hashmap and just wire up neighbor links.
# That’s the whole trick: “create once, reuse forever” keyed by the original node’s identity.

#-----------------------------------Mistakes-------------------------------------------
#You need clone[orig] = cloned because graphs reuse nodes.
# If node 2 is reachable from node 1 and also from node 3, you must ensure both edges in the cloned graph point to the same cloned node 2 (not two different “Node(2)” objects). The hashmap enforces this one-to-one identity mapping:
# original node object → exactly one cloned node object prevents infinite recursion on cycles

#visited isn’t needed because the hashmap itself is the visited set.

#wrong I wrote
# for nei in n.neighbors:
#     newnode.neighbors.append(nei)   # ❌ attaches ORIGINAL node object
#     dfs(nei)                        # ❌ clones it, but you ignore the result
# What it actually builds:
# newnode.neighbors ends up containing pointers to the original graph’s nodes, not the cloned ones.
# So your “clone” is not independent (not a deep copy). It’s a hybrid graph that still points back into the original.
# What it should do:
# dfs(nei) must return the cloned neighbor, and you append that:

