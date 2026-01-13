class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        freshc = 0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    freshc += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q and freshc > 0:
    
            #we use for loop so that even if we append to the queue the current range loop is same original
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    #check out of bounds
                    if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n:
                        continue
                    if grid[r+dr][c+dc] == 1: # fresh - make it rotten
                        grid[r+dr][c+dc] = 2                           
                        q.append((r+dr,c+dc))  # append index, dont do value like this - q.append(grid[r+dr][c+dc])
                        freshc -=1
                        # we dont need a case for rotten oranges
                         #we only need to track the newly rotten in queue
            minutes+=1

        if freshc <= 0:
            return minutes
        else: return -1

        