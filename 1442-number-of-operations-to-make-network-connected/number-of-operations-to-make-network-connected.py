
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n-1:
            return -1

        graph = {i:[] for i in range(n)}
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
   
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for nei in graph[i]:
                if nei not in visit:
                    dfs(nei)
            return

        numofcomp = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                numofcomp +=1
        return numofcomp - 1
        



# #Observation
# --> find cycles, cause u can remove 1 from that
# --> if numofcycles < numofdisconnected components: return -1
#--> here num of cycle can be considered ar numbe rof reduandant edges
# --> else return num of dicosnnected comp
# --> we dont need to find wher eto plug in cables
# -> Also, if  m < n -1, then all nodes cant be connected directly

# During DFS/BFS over ONE connected component:
# nodes = number of vertices visited in this component
# edges = (sum of degrees of visited vertices) // 2
#         (because in an undirected graph each edge contributes +1 degree to TWO endpoints)
# redundant_in_component = edges - (nodes - 1)
#         (a tree on 'nodes' vertices has exactly 'nodes-1' edges; any extra edges must form cycles)
