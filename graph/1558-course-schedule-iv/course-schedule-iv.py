class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 
        #Total time for all queries: O(q⋅(n+m))
        ans = [False]*len(queries) #better to preallocate when size known
        graph = {i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)
        
        visit = set()
        def dfs(u,v): #is u preq of v? so u is source
            if u == v:
                return True
            if (u,v) in visit:
                return False 
            visit.add((u,v)) #cant use continue in if

            for nei in graph[u]:
                if dfs(nei,v):
                    return True  #dont forget this
            return False
  
        for i in range(len(queries)): #dfs per query
            u,v = queries[i][0], queries[i][1]
            ans[i] = dfs(u,v)
            visit.clear() #clear after each use
        return ans

#Start a bfs or dfs from each course i and assign for each course j you visit isReachable[i][j] = True.
#Do this, is=f u have lot of queries, then this better rather tahn doing dfs for every query

#--------------BFS -is reachable  O(n(n+m)+q).---------------------------------
   # isReachable[i][j] = True if i can reach j
        # isReachable = [[False] * numCourses for _ in range(numCourses)]

        # # BFS from each node i
        # for i in range(numCourses):
        #     q = deque([i])
        #     seen = [False] * numCourses
        #     seen[i] = True

        #     while q:
        #         u = q.popleft()
        #         for v in g[u]:
        #             if not seen[v]:
        #                 seen[v] = True
        #                 isReachable[i][v] = True
        #                 q.append(v)

        # return [isReachable[u][v] for u, v in queries]

# ------------------Other methods-----------
# Group by destination + reverse BFS/DFS: Build reverse edges v -> prereqs. For each unique v in queries, one BFS/DFS from v finds all 
# O(K(n+m)+q) with low extra space.

# Floyd–Warshall (transitive closure): Maintain reach[n][n], set direct edges, then run triple loop to propagate reachability. Precompute once in O(n3), answer each query in O(1); uses O(n2) space.