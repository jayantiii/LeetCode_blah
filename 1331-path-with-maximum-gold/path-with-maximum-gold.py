class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        def backtrack(i,j): # max gold start from (i,j)
            if i < 0 or i >= m or j <0 or j>= n:
                return 0

            if (i,j) in visit: #dont forget
                return 0

            if grid[i][j] == 0:
                return 0

            visit.add((i,j))

            top = backtrack(i-1,j)
            down = backtrack(i+1,j)
            left = backtrack(i,j-1)
            right = backtrack(i,j+1)

            visit.remove((i, j)) # IMP!--> FIX 2: backtrack

            return grid[i][j] + max(top, down,left,right)

        maxgold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    gold = backtrack(i,j)
                    maxgold = max(maxgold,gold)

        return maxgold


# #
# Still one critical problem: @lru_cache(None) makes this wrong.

# Reason: dfs(i,j) depends on the current visit set (which cells are already used in the path). But the cache key is only (i,j), so it will reuse an answer computed under a different visit state → wrong results.

        