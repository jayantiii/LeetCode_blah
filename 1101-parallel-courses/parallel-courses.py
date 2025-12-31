class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        indegree = [0]*(n+1) #1based indexing
        for u,v in relations:
            graph[u].append(v)
            indegree[v] +=1

        #Top sort- kahns BFS, find nodes with no preq (can be multiple)
        q = deque()
        for i in range(1,n+1): #(1,N+1)
            if indegree[i] == 0:
                q.append(i)

        semesters = 0
        visitedcourses = 0
        while q:
            size = len(q)
            visitedcourses += size
            for _ in range(size):
                course = q.popleft()
                for nextcourse in graph[course]:
                    indegree[nextcourse] -=1
                    if indegree[nextcourse] == 0:
                            q.append(nextcourse)
            semesters +=1

        
        if visitedcourses != n:
            return -1
        return semesters

# TIP: If total number of courses visited during Kahn's Topological Sort does not equal N (total number of courses), there is a cycle!