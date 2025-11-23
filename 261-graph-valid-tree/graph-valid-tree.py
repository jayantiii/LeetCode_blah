class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # to be tree
        #  - have no cycles - It is fully connected
        #  - edges == n − 1 - DFS/BFS from node 0 visits all n nodes.

        if len(edges) != n-1:return False  #Imp!
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) #both sides

        visit = set()
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for neigh in adj[i]:
                if neigh == prev:
                    continue
                dfsres = dfs(neigh,i)
                if dfsres == False: return False 
                #dont return if true or loop break

        dfs(0,-1)
        return len(visit) == n

#Important to track parent(prev) so that we dont do dfs again on prev in neighbour for loop

    
