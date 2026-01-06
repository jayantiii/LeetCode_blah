class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        WHY WE START AT LAND (1s):
          | Starting at Land (1s)              | Starting at Water (0s)             |
        |------------------|------------------------------------|------------------------------------|
         | Find dist: Water -> nearest Land   | Find dist: Land -> nearest Water   |
         | Water furthest from any land       | Land furthest from any water       |
        | THIS IS WHAT THE PROBLEM ASKS FOR  | THIS IS A DIFFERENT PROBLEM        |
        """
        #Multi Source BFS!
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set() # needed
        water= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: #Imppp - start from 1's!!
                    q.append((i,j))
                    visit.add((i, j))  # mark land visited too
                else:
                    water+=1

        if not q or water == 0:                 
            return -1

        dist = -1 #start from -1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        #Main - The last layer of BFS will be the farthest distance
        # Also, understand that all layers after first will only append ones 1's
        while q:
            size = len(q)
            for i in range(size):
                r,c = q.popleft()
                for x,y in directions:
                    if (r + x) >= 0 and (r+x) < m and (c+y) >=0 and (c+y) < n:
                        if (r+x,c+y) not in visit and grid[r+x][c+y] == 0: #this!
                            q.append((r+x,c+y)) #queue the coordinates!
                            visit.add((r+x,c+y))

            dist +=1

        return dist

#If you start from water cells one by one, you'd have to run a brand new BFS for every single water cell. By starting from land, we use one single BFS run to cover the whole grid.

##----------------Major Mistake----------------------------
# In this problem, we want to find the water cell (0) that is farthest from any land cell (1). To do this efficiently, we should start our BFS from all land cells simultaneously and move outward into the water.

# Enqueue all 1s first ⇒ computes, for each cell, distance to nearest land; answer is max over water of that distance.
# Enqueue all 0s first ⇒ computes, for each cell, distance to nearest water; “last 1” gives max over land of distance to nearest water (a different problem).


# The "Fire" Analogy
# Imagine the land cells (1s) are where a fire starts, and the water cells (0s) are dry grass.
# If you start the fire at all land locations at the same time, the fire will spread to the neighboring grass one step at a time.
# The very last piece of grass to catch fire is the one that was furthest away from any starting point.

#--------------------------------DFS Psuedo but very bad TLE---------------------------
#Imp - No diagonal moves.!!!
# dfs(r,c):
#   if OOB: return INF
#   if grid[r][c] == 1: return 0
#   if visited[r][c]: return INF

#   visited[r][c] = True
#   best = 1 + min(
#       dfs(r-1,c),
#       dfs(r+1,c),
#       dfs(r,c-1),
#       dfs(r,c+1)
#   )
#   visited[r][c] = False
#   return best
