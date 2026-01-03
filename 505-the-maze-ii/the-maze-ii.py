class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        #dist[r][c] = best distance to reach (r,c) (start=0).
        m, n = len(maze), len(maze[0])
        sr,sc = start[0], start[1]
        dr,dc = destination[0], destination[1]

        # #like DP table of minimum distance so far, Dont initialise with zero!!
        dist= [[math.inf]*n for _ in range(m)] 
        dist[sr][sc] = 0

        minheap = [(0,sr,sc)] #(distance, r, c)
        dirs = [(0, 1),(1, 0), (-1, 0), (0, -1)]
        visited = set()
        while minheap:
            d,r,c = heapq.heappop(minheap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == dr and c == dc:
                return d

            for x,y in dirs:
                newx, newy = r ,c #start here
                steps = 0
                #loop until a wall and condition check maze[x + dr][y + dc] this!!
                while 0<= newx + x < m and 0<= newy + y < n and maze[newx + x ][newy + y] == 0: 
                    steps +=1
                    newx = newx + x
                    newy = newy + y
                
                finald = d + steps
                if dist[newx][newy] > finald:
                    dist[newx][newy] = finald
                    heapq.heappush(minheap,(finald,newx,newy))

        return -1


#BFS Djistras's, we use minheap not queue okay!!
# This is a weighted shortest-path problem because each move rolls a variable number of steps; BFS/DFS don’t guarantee minimum total distance, so we run Dijkstra over stopping cells with edge weight = roll length.

# This problem is not plain DFS step-by-step. The “ball” must roll until it hits a wall, so each move has a variable cost (number of cells rolled). That makes it a shortest path on weighted edges → use Dijkstra (min-heap) (or BFS only if all moves had equal cost, which they don’t).

# identifying that this is a dijkstra question and not DP question  is the 90% of the work 

#--------------------DFS SOLnm but not optimal here----------------------------
        # m, n = len(maze), len(maze[0])
        # dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # dist = [[math.inf] * n for _ in range(m)]
        # dist[start[0]][start[1]] = 0

        # def roll(r: int, c: int, dr: int, dc: int):
        #     steps = 0
        #     nr, nc = r, c
        #     # roll until hitting wall or boundary
        #     while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
        #         nr += dr
        #         nc += dc
        #         steps += 1
        #     return nr, nc, steps

        # def dfs(r: int, c: int) -> None:
        #     for dr, dc in dirs:
        #         nr, nc, steps = roll(r, c, dr, dc)
        #         nd = dist[r][c] + steps
        #         if steps > 0 and nd < dist[nr][nc]:
        #             dist[nr][nc] = nd
        #             dfs(nr, nc)

        # dfs(start[0], start[1])

        # ans = dist[destination[0]][destination[1]]
        # return -1 if ans == math.inf else ans
