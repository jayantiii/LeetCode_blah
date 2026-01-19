
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n-1:
            return -1

        graph = {i:[] for i in range(n)}
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
   
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for nei in graph[i]:
                if nei not in visit:
                    dfs(nei)
            return

        numofcomp = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                numofcomp +=1
        return numofcomp - 1

# Intuition / Idea
# - Treat the network as an undirected graph with:
# - Minimum edges needed to connect n nodes is (n - 1).
#   So if m < n - 1 -> impossible -> return -1.

# - Otherwise, we have enough cables in total. We just need to know how many
#   disconnected groups (connected components) there are.

# - If there are c connected components, we need exactly (c - 1) cables to connect them.

# We can always “reuse” extra cables from cycles, so we don’t need to find the exact rewiring. # Answer = c - 1

# Complexity:
# - Build graph + DFS over all nodes/edges: Time O(n + m)
# - Graph + visited: Space O(n + m)   (visited alone is O(n))


#--------------EXTRA - How to find num of redundant edges!!!-------------------
# Let:
#   n = number of nodes
#   m = number of edges
#   c = number of connected components
#
# Minimum edges to keep each component connected (a forest) = n - c
# Redundant edges (extra / cycle edges) = m - (n - c)
#
# Per component:
#   if a component has k nodes and e edges,
#   redundant_in_component = e - (k - 1)

#this gives the number of redundant edges / independent cycles
