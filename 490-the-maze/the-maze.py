class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m , n= len(maze), len(maze[0])
        sr,sc = start[0],start[1]
        dr, dc = destination[0],destination[1]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        def roll(r,c, x,y): #x, y tell which direction we roll
            newr, newc = r,c 
            while newr + x >= 0 and newr + x < m and newc + y >= 0 and newc + y < n:
                if maze[newr + x][newc + y] == 0:
                    newr = newr + x
                    newc = newc + y
                else: #reached wall
                    break
            return newr,newc

        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False

            if r == dr and c == dc:
                return True

            if (r,c) in visited: return False
            visited.add((r,c))

            for x,y in dirs:
                nextr, nextc = roll(r,c,x,y)
                if dfs(nextr,nextc):
                    return True
            return False # no driections worked

        return dfs(sr,sc)

#use plain dfs or bfs
# You separate roll() because it’s the core move rule in this problem: “from a stop-cell, keep moving until the next step would hit a wall, then stop there.” You’ll call that same logic 4× per state. Keeping it in a helper avoids copy-paste bugs and makes DFS code readable.

#follow-up to return the actual path to the destination.
