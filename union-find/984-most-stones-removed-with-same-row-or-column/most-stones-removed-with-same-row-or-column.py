class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = {} #stores indices
        cols = {}
        visited = set() #store indices
        for i in range(len(stones)):
            x,y = stones[i]
            rows.setdefault(x, []).append(i)
            cols.setdefault(y, []).append(i)

        #DFS should take a stone index (not (x,y)), because you need to mark stones visited.         
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for x in rows[stones[i][0]]:
                dfs(x)
            rows[stones[i][0]] = []  # clear after use
            for y in cols[stones[i][1]]:
                dfs(y)
            cols[stones[i][1]] = []  # clear after use so u dont go again and again
                  
        components = 0
        for i in range(len(stones)):
            if i in visited:
                continue
            dfs(i)
            components +=1

        return len(stones) - components
        #Main #number of stones - no. of connected components

# to figure out the intuition - that component will form with same row and col stones and then we can always remove all stones left 1 at last but how to make componenets in implementation is tricky

# DFS clue: think connected components.
# Make a graph where stones are nodes.
# Edge between stone i and j if they share row or column.
# In any connected component of size k, u can remove k-1, leaving 1

# HINT 1 :
# Instead of viewing this question as "Remove the maximum number of stones with the same rows and columns", you may take this question to be "What is the number of stones that can be reached from one another, if reaching stone A to stone B requires either stone A and B having same row or column.


##--------------------------------- Union Solution---------------------------------------
# Union-Find (DSU) approach (mental model in comments)
#
# Model stones as edges in a bipartite graph:
#   Left side nodes  = row values (x)
#   Right side nodes = column values (y)
#   Each stone (x, y) creates an edge between row-node x and col-node y.
#
# Key observation:
#   Within one connected component of this row/col graph, you can remove all stones
#   except one (because removals are possible as long as there is another stone
#   sharing a row/col in that component).
#   => If a component has k stones, removable = k - 1.
#   => Total removable = n - (#connected_components).
#
# DSU plan:
#   1) Union(row x, col y) for every stone (connect the row-node and col-node).
#   2) Count how many distinct DSU roots exist among ONLY the nodes that actually appear.
#      (i.e., rows/cols present in the input).
#   3) Answer = n - component_count.

###CODEEEEE---
# class DSU:
#     def __init__(self):
#         self.parent = {}
#         self.rank = {}

#     def find(self, x):
#         if x not in self.parent:
#             self.parent[x] = x
#             self.rank[x] = 0
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, a, b):
#         ra, rb = self.find(a), self.find(b)
#         if ra == rb:
#             return
#         if self.rank[ra] < self.rank[rb]:
#             ra, rb = rb, ra
#         self.parent[rb] = ra
#         if self.rank[ra] == self.rank[rb]:
#             self.rank[ra] += 1

# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         dsu = DSU()
#         used_nodes = set()

#         for x, y in stones:
#             rx = ("r", x)   # row node
#             cy = ("c", y)   # col node
#             dsu.union(rx, cy)
#             used_nodes.add(rx)
#             used_nodes.add(cy)

#         components = len({dsu.find(node) for node in used_nodes})
#         return len(stones) - components
