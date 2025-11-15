class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#For networkDelayTime, you really want Dijkstra’s algorithm with a min-heap, not DFS.
#whenever you see “single-source shortest path, positive weights”, your brain should Dijkstra with priority queue.

        # the max time by a k to a node is the final answer
        adj = { i:[] for i in range(n+1)}  # n+1 cause it says 1..n notice
        for u,v,w in times:
            adj[u].append([v,w])

        visit = set()      
        #array for times from k to node
        mintimes = [float('inf')]*(n+1)

        def dfs(k, timetoreach):
            #base
            if mintimes[k] <= timetoreach:
                return    
            mintimes[k] = timetoreach
            visit.add(k)
            for neigh, time in adj[k]:
                dfs(neigh, timetoreach + time)
        
        dfs(k,0) #k to k is 0

        if len(visit) != n: 
            return -1

        #If you use 1-based indexing, you should not include mintimes[0]:
        return max(mintimes[1:])

        