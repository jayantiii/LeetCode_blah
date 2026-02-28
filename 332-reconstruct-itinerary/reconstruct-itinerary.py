class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        res = []
        for u,v in tickets:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)

        for node in graph:
            graph[node].sort() # cant sort on queue
            graph[node] = deque(graph[node])

        def dfs(node):
            #Imp to use while loop! USING FOR NOT GOOD - cause we change graph
            while node in graph and  graph[node]:
                nei = graph[node].popleft()
                dfs(nei)

            res.append(node) #IMP - append after while not inside!


        dfs("JFK")
        return res[::-1] #Reverse needed - think

#Points
# In DFS postorder solutions for Eulerian paths, you almost 
#always reverse at the end to get the correct order. 
# You can avoid reversal only if you prepend or use a stack, but bad

# We append after the while because we only know the correct position of an 
#airport after using all its outgoing tickets.

# we use a deque and popleft, but the standard solution reverse-sorts lists
#  and pops from the end to keep the code simpler while maintaining the
# same complexity. --> # graph[node].sort(reverse=True)