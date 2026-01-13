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


#-------------------Critical Mistake: Dont use lru_cache!!!-----------------
#-->  @lru_cache(None) makes this wrong.
# @lru_cache will compute dfs(i,j) once (under whatever visit state happened first) and then reuse it for the other case, which is wrong.
# lru_cache assumes: same inputs ⇒ same answer. But your dfs(i,j) answer is not determined only by (i,j). It also depends on which cells are already in visit

# Reason: dfs(i,j) depends on the current visit set (which cells are already used in the path). But the cache key is only (i,j), so it will reuse an answer computed under a different visit state → wrong results.

#------------When do u need  visit.remove((i, j)) and not?---------------------------
# Quick mental test
# Ask: “After returning from exploring one option, do I want the next option to act as if this choice never happened?”
# If yes → you must undo it (remove / restore) or pass a copied state.
# If no (global processed) → you don’t remove.

# You don’t need remove when:
# visited is meant to be global “already processed”, not path-local
# Examples: connected components / island counting, graph traversal to avoid reprocessing nodes.

# You don’t mutate shared state (you pass a fresh state down)
# Example: dfs(next, visited | {next}) creates a new set, so there’s nothing to undo.

# DP/memoization where the state is fully in the arguments
# Example: dp(i,j) for grid paths when revisits are allowed or irrelevant; no visit needed.

#----------------Backtrack vs dfs-----------------------------------------
# Backtracking isn’t a different algorithm from DFS. It’s just DFS + undo.
# DFS explores one choice, goes deeper, then comes back. Backtracking is the step where you revert the choice (like visit.remove(...)) so the next branch starts clean.

    