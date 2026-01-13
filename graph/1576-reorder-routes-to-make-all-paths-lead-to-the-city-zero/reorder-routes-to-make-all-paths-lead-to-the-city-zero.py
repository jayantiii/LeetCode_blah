class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)} # dont use len(connections) as its no of edges
        for u,v in connections:
            adj[u].append([v,1]) #existing edge
            adj[v].append([u,0]) #reverse edge
        edges = 0
        visit = set()
        visit.add(0)
        def dfs(node):
            nonlocal edges
                # no base condition needed here
            for neigh, dir in adj[node]: # unpack here
                if neigh not in visit:  #dont use return here, it then wont go to all neigh
                    edges += dir
                    visit.add(neigh)
                    dfs(neigh)
            return
                

        dfs(0)
        return edges

  
#Note - You built an undirected tree (each connection added twice). If you don’t track where you came from, DFS can bounce back and forth forever

    #BFS WAY, works too
        
        # adj = { i:[] for i in range(n)} # dont use len(connections) as its no of edges
        # for u,v in connections:
        #     adj[u].append([v,1])
        #     adj[v].append([u,0]) #reversed


        # queue = deque([])
        # queue.append(0)
        # visit = set()
        # visit.add(0) # dont forget this
        # edges = 0
        # while queue:
        #     node = queue.popleft()
        #     for neigh, dir in adj[node]:
        #         if neigh not in visit:
        #             visit.add(neigh)
        #             edges += dir
        #             queue.append(neigh)

        # return edges


        