class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = { i:[] for i in range(n)}
        degree = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] +=1
            degree[v] +=1

        #Find leaves and add in queue
        remaining = n
        q = deque()
        for node in graph:
            if len(graph[node]) == 1: #only 1 edge, degree 1
                q.append(node)
                #dont remove degree here, will break logic
        
        while remaining > 2: #if last 2 or 1 left, those are centers
            size = len(q) #layer wise
            remaining -= size
            degree[node] = 0     # mark leaf as removed (optional)
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    if degree[nei] > 0:    # only update nodes still in the tree
                        degree[nei] -=1 # Imp - reduce first and then check
                        if degree[nei] == 1:
                            q.append(nei)

        return list(q)
         # just return list(q), Remaining nodes in queue are centers

#“Where should I root the tree so that its height is as small as possible?”
#“The height of a rooted tree is the number of edges on the longest path from the root to a leaf.”

#Solution Idea
# For any tree, the root(s) that give minimum height are exactly the center(s) of the tree.
# A tree has either:
# 1 center (for odd-length diameter), or
# 2 centers (for even-length diameter).
# This problem = find all centers of the tree.
# Centers = nodes that, when used as root, minimize tree height.

# Intuition:
# Think about the longest path in the tree (the diameter).
# If you root the tree at one end of the diameter, height is big.
# If you root near the middle of that diameter, height shrinks.
# The position(s) in the middle of the diameter give the minimum poss

##--------------Two ways to find the center--------------------------------------
# -- 1) Leaf peeling algo to find center, Example----
0 - 1 - 2 - 3 - 4
# Heights if rooted at each node:
# Root at 0 → distances: [0,1,2,3,4] → height = 4
# Root at 1 → [1,0,1,2,3] → height = 3
# Root at 2 → [2,1,0,1,2] → height = 2 ✅
# Root at 3 → symmetric to node 1 → height = 3
# Root at 4 → symmetric to node 0 → height = 4
# Minimum height = 2, achieved only at node 2 → center = {2}.
# Peeling algorithm:
# Leaves initially: {0,4}
# Remove them → new leaves: {1,3}
# Remove them → remaining: {2}
# Answer: [2]

#---2) Two BFS---------------------------------
# You can also get the center(s) using a different BFS-based approach via the tree diameter.
# Pick any node u (e.g., 0).
# Run BFS from u to find the farthest node A.
# Run BFS from A to find the farthest node B and record the path A → ... → B.
# The path A → ... → B is a diameter of the tree.
# The centers are the middle one or two nodes on this diameter path.
# Why this works:
# In a tree, BFS from any node will end at one of the diameter endpoints.
# BFS again from that endpoint gives you the full diameter.
# Middle of the diameter = center(s).

#---------------------- Brute force idea (why it’s bad)
# Naive thought:
# For every node x from 0 to n-1:
# Treat x as root.
# Run BFS from x to compute the height = max distance to any node.
# Take all x with minimal height.
# Complexity:
# One BFS: O(n) (tree has n-1 edges).
# Do BFS from all n nodes → O(n^2).


#---------My mistakes while coding ----------------------
#1) I tried finding remaining nodes at last using a loop, but not needed, just return q
#In a star tree, after peeling all leaves, the center’s degree becomes 0, not 1. so wrong answer too
#   res = []
#         for i in range(n):
#             if degree[i] == 1: #left node
#                 res.append(i)
#         return res

#2) In the while loop, I kept mixing where to reduce degree, where to reduce remaining , be careful and think
# how to structure

# 3) I did like this below, which is okay but not necessary , simplify it
#   for i in range(size):
#                 node = q.popleft()
#                 degree[node] -=1 #dont forget,  #if we make degree = 0, consider leaf removed
#                 remaining -=1 #update this here, not in next loop

