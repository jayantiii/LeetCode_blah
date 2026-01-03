class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 
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
            visit.add((u,v))

            for nei in graph[u]:
                if dfs(nei,v):
                    return True  #dont forget this
            return False
  
        for i in range(len(queries)):
            u,v = queries[i][0], queries[i][1]
            ans[i] = dfs(u,v)
            visit.clear() #clear after each use
        return ans

    

#Start a bfs or dfs from each course i and assign for each course j you visit isReachable[i][j] = True.