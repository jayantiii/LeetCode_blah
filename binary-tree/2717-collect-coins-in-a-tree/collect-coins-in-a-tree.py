class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(len(coins))}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        #Step1 - remove leaves with no coins ( pruning) leaf ⇒ degree = 1
        q = deque()
        for node in graph: # add all leaves to queue
            if len(graph[node]) == 1 and coins[node] == 0:
                q.append(node)
       
        while q: # #Bfs, process all nodes in q
            node = q.popleft()
            for nei in graph[node]: 
                graph[nei].remove(node) #remove node from neighbour
                if len(graph[nei]) == 1 and coins[nei] == 0:
                    #remove leaf from graph and add new leaf to the queue
                    q.append(nei)
            graph[node].clear()  # correct way


        #Step2 - peel last 2 layers because they can be reached without using edges
        q = deque()
        for node in graph:
            if len(graph[node]) == 1:
                q.append(node)
        i=2
        while i>0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    graph[nei].remove(node) #syntax!
                    if len(graph[nei]) == 1:
                        q.append(nei)
                graph[node].clear()   #dont use del since graph is being actively used
            i-=1

        #Step3 - Total would be 2 * (number of edges)
        # as one for going front and on for going back to start
        # sum of degrees of all nodes  =  2 * (number of edges)
        sumdegree = 0
        for node in graph:
            sumdegree  +=  len(graph[node])

        return sumdegree





        
#Hint - Remove the leaves that do not have coins on them, so that the resulting tree will have a coin on every leaf.

#--------------------My mistakes while coding-----------------------------
# You do not need to “pick the ideal starting point” explicitly. The pruning logic is designed so that once you compute the remaining core, the minimum walk length is determined only by how many edges are left — not by where you start.

#I tried using Dfs for leaf pruning, “leafness” in this problem is dynamic. Once you remove some leaves, new leaves appear. DFS from 0 is wrong because the relevant subtree may not even include 0. You need a BFS / queue-based pruning process, repeatedly removing coinless leaves, not one-time DFS. Also you must not “delete node by node inside recursion” because the graph mutates. as you prune nodes, their neighbors’ degrees change, and new leaves appear. This changing-leaf behavior is the entire reason DFS fails.

# One better alternative to my correct method instaed of delete nodes in graph and counting edges in graph and all that is to have a seperate degree[i] array and update that

# for node in graph:
#     del graph[node], You CANNOT delete from graph while iterating it
# We  can instead maintain degree[] array and set degree to 0 when removed. Just a suggestion

# You’re removing only ONE leaf per while loop pass
# You must remove all current leaves, not one.
# When you “remove” a leaf, you MUST decrease degree of its neighbor.
# Without doing that, the next leaf layer never forms correctly.


