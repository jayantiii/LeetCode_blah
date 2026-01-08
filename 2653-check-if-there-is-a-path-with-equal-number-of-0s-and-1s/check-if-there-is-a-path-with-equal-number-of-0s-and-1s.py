class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        L = m + n - 1

        # Need equal #0 and #1 on the path -> path length must be even
        if L % 2 == 1:
            return False

        @lru_cache(None)
        def dfs(i,j,zc,oc): #return True if there is a equal path from start to end
            if  i >=m or  j >=n:
                return False
     
           #Count current cell
            zc += 1 if grid[i][j] == 0 else 0
            oc += 1 if grid[i][j] == 1 else 0

            if i == m-1 and j ==n-1:
                return zc == oc

            down = dfs(i+1,j,zc,oc)
            right = dfs(i,j+1,zc,oc)

            return down or right

        return dfs(0,0,0,0)

        