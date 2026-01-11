class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = [-1] * len(queries)
        graph = {}
        for i in range(len(equations)):
            num,denum = equations[i]
            if num not in graph:
                graph[num] = []

            if denum not in graph:
                graph[denum] = []

            graph[num].append((denum,values[i]))
            graph[denum].append((num,1/values[i]))

        visit = set()
        def dfs(source,target,curr):

            if source not in graph or target not in graph:
                return -1.0

            if source == target:
                return curr

            visit.add(source)

            for var,val in graph[source]:
                if var in visit:
                    continue
                answer = dfs(var,target,curr*val)
                if answer != -1.0:
                    return answer

            return -1
         

        for i in range(len(queries)):
            num = queries[i][0]
            denum = queries[i][1]
            ans = dfs(num, denum,1)

            visit.clear()
            res[i] = ans

        return res
            
        