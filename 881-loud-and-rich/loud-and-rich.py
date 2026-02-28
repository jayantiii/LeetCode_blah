class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        answer = [i for i in range(n)] #each think they are the queitest
        graph = {i:[] for i in range(n)}
        indegree = [0 for i in range(n)]
        for u,v in richer:
            graph[u].append(v)
            indegree[v] +=1

        queue = deque() #add all with indegree 0
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft() #means we have correct answer for node!
            for nei in graph[node]:
                if quiet[answer[node]] < quiet[answer[nei]]: #IMP-THIS!!
                    answer[nei] = answer[node]

                indegree[nei] -=1
                if indegree[nei] == 0: #only then append!
                    queue.append(nei)

        return answer

        

# For person x, you only consider:
# x themself
# anyone who is richer than x (directly or indirectly)
# IMP -> You do NOT consider people who are unrelated or poorer.  

# For topological order we want: richer → poorer
# Because richer people must be processed before poorer ones