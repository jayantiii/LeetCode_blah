class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#Maximum time along any path from headID down to a leaf, where edge cost = informTime of the parent.
        
        adj = {i:[] for i in range(len(manager))}
        for i in range(len(manager)):
            if manager[i] == -1: #headid
                continue
            adj[manager[i]].append(i)
        def dfs(manager):
            
            if not adj[manager]:
                return 0 #have no child
               
            ## Time to inform whole subtree = time to inform direct subs
            # + maximum time among children's subtrees
            max_child_time =0
            for child in adj[manager]:
                childtime = dfs(child)
                max_child_time = max(max_child_time ,childtime)
                
            return informTime[manager] + max_child_time
                 
        return dfs(headID)
        
        