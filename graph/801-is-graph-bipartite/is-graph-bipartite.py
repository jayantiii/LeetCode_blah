class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
#  2 colorable,algo can be like colour the nodes alternate and if there is a contradiction
#graph is in adj list form
#1 - c -- helps in reversing colors
        
        n = len(graph) # number of nodes
        color = [-1] * n # color 0 or 1
        
        def dfs(i: int,c: int) -> bool:
            color[i] = c # assign the color

            # loop through neighbours
            for neigh in graph[i]:
                if color[neigh] == -1:
                    dfsres =  dfs(neigh, 1-c) # run dfs on neighbour
                    if not dfsres: 
                        return False #dont return dfsres, if its true, for loop wont run for all adj
                elif color[neigh] == color[i]:
                    return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                dfsres = dfs(i,0)
                if not dfsres: return False # dont forget this

        return True
        





# We use a color array initialized with -1 for all nodes (meaning unvisited).
# Start DFS from each unvisited node and try coloring it with 0 or 1.
# During DFS:
# If the neighbor is uncolored → recursively color it with opposite color.
# If the neighbor has the same color → ❌ Not bipartite.
# If we succeed in coloring the entire graph without conflicts → ✅ Bipartite!

# Time Complexity: O(V+E)
# Every node and edge is visited once in DFS.

# Space Complexity: O(V)
# For the color array and recursive stack.