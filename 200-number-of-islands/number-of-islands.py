class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#use dfs or bfs to traverse || O(m,n)
    
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
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r, c-1)

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