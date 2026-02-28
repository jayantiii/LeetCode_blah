class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
 
        def dfs(i,comp):
            if i in visited:
                return

            visited.add(i)
            comp.append(i) #store the component!

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei,comp)


        count = 0
        for i in range(n):
            if i not in visited:
                comp = []
                dfs(i,comp)

                size = len(comp)
                complete = True
                for node in comp:
                    if len(graph[node]) != size-1:
                        complete = False
                        break

                if complete: 
                    count+=1

        return count

#A complete component of size k must have:
# k * (k - 1) / 2 edges

#My first mistake!
# 0 — 1 — 2
# This is connected → you count it ✅
# But it’s not complete, because edge (0,2) is missing ❌

#ways to fix
#1)Count edges in the component and compare to formula.
#2)Check if each node’s degree inside the component equals size - 1.