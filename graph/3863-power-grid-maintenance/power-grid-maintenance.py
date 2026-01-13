class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ## Time: O(c + m + c log c) = O((c + m) + c log c)
        res = []  # only store answers for type-1 queries
        onlinestations = set(range(1,c+1))
        graph = {i:[] for i in range(1,c+1)} # O(c + m)

        for u,v in connections: 
            graph[u].append(v)
            graph[v].append(u)

        #Find all SCCs
        visited = set()
        comp_idlist = [-1] * (c + 1)     # comp_id[i] = component index of node i
        groups = {}   #{compid - [heap]}
        comp_id = 0
        def dfs(node,compid):
            if node in visited:return
            if compid not in groups:
                groups[comp_id] = []
            heapq.heappush(groups[compid],node) #imp
            comp_idlist[node] = compid
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei,comp_id)

        for node in range(1,c+1):
            if node in visited:
                continue
            dfs(node,comp_id)
            comp_id +=1

        #Process the queries
        for i in range(len(queries)):
            number = queries[i][0]
            station = queries[i][1]

            if number == 1:
                if station in onlinestations:
                    res.append(station)
                else:
                    #Find the smallest in the whole component and that is online
                    compid = comp_idlist[station] # we get the component id
                    nodes = groups[compid] # we get all nodes in component in heap form
                    
                    # lazy-delete offline nodes from heap top
                    while nodes and nodes[0] not in onlinestations :
                        heapq.heappop(nodes)

                    if nodes: #Nodes meaning the minheap
                        smallest = nodes[0] # just peek, dont pop!!!
                        res.append(smallest)
                    else: res.append(-1)
                        
            if number == 2 and station in onlinestations:
                onlinestations.remove(station)

        return res

#Important, Big questions try again!! --
#we need store all strongly connected components
#Also, we need heaps for each SCC 
#-------------My one big mistake-----------------------------
# You’re getting -1 where the judge wants 1 because the problem is not “smallest online neighbor”, it’s “smallest online station in the same connected component (grid), even through offline nodes”. But I coded for smallest neighbour.

# My Heap logic was wrong for online nodes.
# You heappop even when smallest is online. Then this node disappears from the heap, so later queries in the same component can’t see it anymore. You only want to pop offline nodes; for online ones you should just peek.

#-------------Suggestion-----------------------------------------       
# Use discard instead of if station in ...: remove. for set
# discard avoids the explicit membership check.

# For each station, know which connected component it belongs to, and be able to access all nodes in that component.# Two standard ways:
# Precompute components with DFS/BFS and assign a comp_id to each node.
# Use DSU (Disjoint Set Union / Union-Find) and group nodes by their root.

#----------------------Union Find soln, see how -----------------------------
# class Solution:
#     def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
#         parent = list(range(c + 1))

#         def find(x):
#             while x != parent[x]:
#                 parent[x] = parent[parent[x]]
#                 x = parent[x]
#             return x

#         def union(x, y):
#             px, py = find(x), find(y)
#             if px != py:
#                 parent[py] = px

#         for u, v in connections:
#             union(u, v)

#         components = defaultdict(list)
#         for i in range(1, c + 1):
#             heapq.heappush(components[find(i)], i)

#         online_check = [1] * (c + 1)
#         res = []

#         for t, x in queries:
#             if t == 1:
#                 if online_check[x]:
#                     res.append(x)
#                 else:
#                     comp = components[find(x)]
#                     while comp and not online_check[comp[0]]:
#                         heapq.heappop(comp)
#                     res.append(comp[0] if comp else -1)
#             else:
#                 online_check[x] = 0
#         return res

# The union-find solution is conceptually the same idea but:
# Instead of DFS to find components,
# You use Disjoint Set Union (DSU / Union-Find) to build components.

#------------------------------ExPLAINATION OF tIME OF dfS SOLN----------------------
#  """
#         c = number of stations (nodes)
#         m = number of connections (edges)
#         Q = number of queries

#         Preprocessing:
#         1) Build adjacency list `graph`:
#            - Create dict for 1..c        → O(c)
#            - Add each undirected edge    → O(m)
#            => O(c + m)

#         2) DFS over graph to find components:
#            - Visit each node once        → O(c)
#            - Traverse each edge twice    → O(m)
#            => O(c + m)

#         3) For each node, push into its component heap:
#            - Each node heappush once     → O(log c) per node worst-case
#            - Total nodes = c             → O(c log c)

#         => Total preprocessing time:
#            O(c + m) [graph] + O(c + m) [DFS] + O(c log c) [heaps]
#            = O(c + m + c log c)
#            = O((c + m) + c log c)

#         Query phase (for completeness):
#         - Type-2 queries: mark offline       → O(1) each → O(Q)
#         - Type-1 queries:
#             * constant work per query
#             * plus pops from heaps (lazy deletion):
#               each node popped at most once → O(c log c) over all queries
#           => O(Q + c log c)

#         Overall:
#         - Time ≈ O(c + m + Q + c log c) = O((c + m + Q) log c) in big-O form
#         - Space: O(c + m) for graph + arrays + heaps
#         """