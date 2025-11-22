class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Think that You can do bfs from each gate simultaneously!!
        m = len(rooms)
        n = len(rooms[0])
        def addroom(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or rooms[i][j] == -1 or (i,j) in visit:return
            q.append((i,j))
            visit.add((i,j))
       
        q = deque([])
        visit = set() # here visit set will work out but not in dfs
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j)) # append indices not values
                    visit.add((i,j))
        dist = 0
        while q:
            # pop all at once
            for x in range(len(q)):
                i,j = q.popleft() #do popleft
                rooms[i][j] = dist
                addroom(i+1,j)
                addroom(i-1,j)
                addroom(i,j-1)
                addroom(i,j+1)
            dist+=1
        return rooms

#Dont forget to add to visit , then again also dont forget to check if in visit

#DFS works!! not optimal, CAUSE TLE FOR LAST test case, 
# Worst-case time: O((R·C)²)
# A trivial safe upper bound is O(G · R · C):
# Each DFS can, in the worst arrangement, visit O(R·C) cells before being fully pruned.
# Since G(gates) can be O(R·C) in the worst case (a gate in every cell):

# Space: O(R·C) due to recursion depth.

        # INF = pow(2,31) -1
        # m = len(rooms)
        # n = len(rooms[0])

        # def dfs(i,j,dist):
        #     if i < 0 or j < 0 or i >=m or j >=n or rooms[i][j] == -1:
        #         return   
        #     #You must STOP recursion when the current cell already has a smaller or equal
        #     if rooms[i][j] <dist: return 
                
        #     rooms[i][j] = dist

        #     dfs(i+1,j,dist +1)
        #     dfs(i-1,j, dist +1)
        #     dfs(i,j-1, dist +1)
        #     dfs(i,j+1, dist +1)

        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == 0: # from every gate
        #             dfs(i,j,0)
        # # no visit set cause, we need to find minimum
        