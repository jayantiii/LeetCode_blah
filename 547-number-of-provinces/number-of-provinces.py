class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #input is adj matrix
        #find total number of disconnected components

        visit = set()
        count= 0
        def dfs(i):
            if i in visit: return
            visit.add(i)
            for neigh in range(len(isConnected)):
                if isConnected[i][neigh] == 1 and neigh != i:
                    dfs(neigh)


        for i in range(len(isConnected)): #loop though each node and perform dfs
            if i not in visit:
                dfs(i)
                count+=1
        return count