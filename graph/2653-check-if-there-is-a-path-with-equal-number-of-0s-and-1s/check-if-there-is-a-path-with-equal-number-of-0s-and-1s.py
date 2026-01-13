class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        # Time:  O(m*n*L)
        m = len(grid)
        n = len(grid[0])
        L = m + n - 1

        # Need equal #0 and #1 on the path -> path length must be even
        if L % 2 == 1:
            return False

        # return True if there is a equal path from start to end
        @lru_cache(None)
        def dfs(i,j,zc,oc): 
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

# No "remove/backtrack" needed for zc/oc:!!!
# - zc and oc are ints (immutable).
# - `zc += 1` makes a NEW int for THIS call frame; it doesn't change caller's zc.
# - when the call returns, its local zc/oc disappear automatically.
# Backtracking is only needed for shared mutable stuff (list/set/dict/grid edits).

# -------------Why dp[i][j] = True/False is not enough:--------------------
# - Same cell (i,j) can be reached with different counts of 1s so far.
# - Whether we can finish with equal 0s/1s depends on that count.
# - A boolean dp[i][j] collapses different counts into one => loses info => wrong.
# - Need dp that tracks "ones so far" (set/bitset) or DFS state includes count.

#---------- Time/Space for cached DFS dfs(i,j,zc,oc):------------------------
# - Total states sum_{i,j} O(i+j) = O(m*n*(m+n)) = O(m*n*L), where L = m+n-1

# - Time:  O(m*n*L)
# - Space: O(m*n*L) for cache + O(L) recursion stack

# Because L = m + n - 1 is the maximum number of cells on any full path, and (i + j + 1) is the number of cells visited so far at cell (i,j).
#at (i,j) you always have zc + oc = i + j + 1
# - You can cache (i,j,oc) instead of (i,j,zc,oc) since zc = (i+j+1)-oc.

# At the same cell (i,j), you can arrive with different (zc,oc) counts, and lru_cache will store a separate entry for each distinct tuple.
# So per (i,j), the number of distinct cached states is about the number of possible oc values: O(i+j), up to O(L).

#----------------Some observations-----------------------
# Any path from (0,0) to (m-1,n-1) visits exactly:
#   L = m + n - 1
# cells (because you make (m-1) downs + (n-1) rights = m+n-2 moves,
# and cells visited = moves + 1 = m+n-1).
#
# To have equal number of 0s and 1s on the path:
#   L must be even
#   ones must be exactly L//2   (and zeros also L//2)
#
# If L is odd -> impossible -> return False immediately.



        