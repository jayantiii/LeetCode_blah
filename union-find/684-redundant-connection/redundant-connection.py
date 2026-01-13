class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1,len(edges)+1)}
        visited = set()
        def isreachable(u,v): #is v reachable from u
            if u == v:
                return True

            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    if isreachable(nei,v): return True
            return False #return false here

        for u,v in edges:
            visited.clear()          # reset for this reachability check
            if isreachable(u,v): #then adding this is cycle
                return [u,v]
            visited
            #add edge
            graph[u].append(v)
            graph[v].append(u)


# Build the graph incrementally.
# For each new edge (u, v):
# Before adding it, check if u can already reach v in the current graph (DFS/BFS).
# If yes → adding (u, v) creates a cycle → return (u, v).
# Else add the edge and continue.
# Why it works: the only way an added edge is redundant is if its endpoints already have a path between them.

# --------------------Time Complexity (incremental DFS reachability):
# - There are n edges.
# - For each edge, we may run a DFS over the current graph (up to O(n) nodes/edges).
# - Worst-case total: O(n^2).
#
# Space Complexity:
# - Graph adjacency list: O(n)
# - visited set per DFS: O(n)
# - Recursion stack worst-case: O(n)
# => Overall: O(n)

#--------------------- Some of my bugs-------------------
# visited must be fresh for each reachability check. Right now it persists across edges, so later checks get wrong “already visited” behavior.

# Inside the loop you do:# return isreachable(nei, v)
# This returns after the first neighbor only. If the path is through a different neighbor, you’ll incorrectly return False. You must keep searching and return True if any neighbor reaches v.

# ------------------------Why time is O(n^2) for incremental DFS:-----
# - For each edge, we run a DFS to check if v is reachable from u in the current graph.
# - Before processing edge i, the graph already has about (i-1) edges (almost a tree).
# - In the worst case, the DFS may scan O(i-1) edges/nodes.
# - Total work over all edges:
#     1 + 2 + 3 + ... + (n-1) = (n-1)*n/2 = O(n^2)

##------------Union Solution, Time: ~ O(n α(n)) (almost linear) ----------------------
#Space: O(n)
# Use Union-Find (DSU):
# Start with each node in its own set.
# For each edge (u, v) in order:
# If find(u) == find(v), then u and v are already connected → adding this edge forms a cycle → this edge is the redundant one → return it.
# Else union(u, v).
# That’s the whole trick. Time ~ O(n α(n)).

# class DSU:
#     def __init__(self, n: int):
#         self.parent = list(range(n + 1))
#         self.rank = [0] * (n + 1)

#     def find(self, x: int) -> int:
#         # path compression
#         while self.parent[x] != x:
#             self.parent[x] = self.parent[self.parent[x]]
#             x = self.parent[x]
#         return x

#     def union(self, a: int, b: int) -> bool:
#         # returns False if already in same set (cycle edge), True if merged
#         ra, rb = self.find(a), self.find(b)
#         if ra == rb:
#             return False

#         # union by rank
#         if self.rank[ra] < self.rank[rb]:
#             ra, rb = rb, ra
#         self.parent[rb] = ra
#         if self.rank[ra] == self.rank[rb]:
#             self.rank[ra] += 1
#         return True


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         n = len(edges)
#         dsu = DSU(n)

#         for u, v in edges:
#             if not dsu.union(u, v):   # u and v already connected -> redundant
#                 return [u, v]
