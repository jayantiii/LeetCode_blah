class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#use dfs or bfs to traverse || time -O(m,n)
# space - m × n - cause in worst case all 1's grid, call stack will have all cells
    
        m,n = len(grid), len(grid[0])
        count = 0
        # visited = set().  - not needed for this
        def dfs(r,c):

            if r < 0 or c < 0 or r >= m or c >= n: #recursion!, no need to check r+1,c+1
                return
            if grid[r][c] == "1": # needed here too
                grid[r][c] = "#" #if we dont do this,  then we need visited set
            else:
                return

            # even if some coordinates generated can be not valid, we have initial check
            dfs(r+1,c) #down
            dfs(r-1,c) # up
            dfs(r,c+1) # right
            dfs(r, c-1) # left

            #wrong --- dfs(r+1,c+1) is diagnal
            
        for r in range(m):  #use m and n, not directly gri
            for c in range(n):
                if grid[r][c] == "1": # this needed here also and in dfs too
                    count +=1 # we change the 1 to 0/# so dw count wont increase everytime
                    dfs(r,c) # runs only when '1'

        return count

#note count += is diff then count =+
# == diff than = ( dont switch)
# r >= m or c >= n --- its not just >

# “The brute force solution is: for each cell in the grid, if it is land, run a full DFS/BFS from that cell to explore the entire connected island. But since we don’t mark visited cells, each island gets explored many times — once for every land cell inside it. That makes the brute force extremely slow because the same region is repeatedly traversed.” leading to O((m·n)²) time complexity

from typing import List
import collections

#BFS WAY - more hard not needed
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # islands = 0

        # def bfs(r, c):
        #     q = collections.deque()
        #     q.append((r, c))
        #     visit.add((r, c))

        #     while q:
        #         row, col = q.popleft()

        #         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc

        #             # bounds + land + not visited
        #             if (
        #                 0 <= nr < rows and
        #                 0 <= nc < cols and
        #                 grid[nr][nc] == "1" and
        #                 (nr, nc) not in visit
        #             ):
        #                 visit.add((nr, nc))
        #                 q.append((nr, nc))

        # # Scan grid
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visit:
        #             islands += 1
        #             bfs(r, c)

        # return islands
