class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #down or right
        m = len(grid)
        n = len(grid[0])
        dprow = [float('inf')] * n   # use inf not zero!!
        for i in range(m):
            newrow = [0]*n
            for j in range(n):
                if i == 0 and j == 0: #this necessary case
                    newrow[j] = grid[0][0]
                else:
                    topcell = dprow[j] if i > 0 else float('inf') #read from dprow not grid
                    leftcell = newrow[j-1] if j >0 else float('inf') #read from newrow
                    newrow[j] = min(topcell,leftcell)+grid[i][j]
            dprow = newrow
            print(dprow)

        return dprow[-1]

#topcell = dprow[j] if i > 0 else float('inf') --- USE INF NOT ZERO!!!
# Using 0 there makes “no path” look better than any real path, so the DP never accumulates cost along the first row / first column.

#similar answer without any space, from deepti video
#   for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if row == 0 and col != 0:
#                     grid[row][col] += grid[row][col - 1]
#                 elif col == 0 and row != 0:
#                     grid[row][col] += grid[row - 1][col]
#                 elif row != 0 and col != 0:
#                     grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
#         return grid[-1][-1]

#Top down recueive approach
    # m, n = len(grid), len(grid[0])
    #     memo = {}

    #     def dfs(i, j):
    #         # Out of bounds → impossible path, return +inf so it never gets chosen
    #         if i < 0 or j < 0:
    #             return float('inf')

    #         # Base case: starting cell
    #         if i == 0 and j == 0:
    #             return grid[0][0]

    #         # Memoized result
    #         if (i, j) in memo:
    #             return memo[(i, j)]

    #         # Recurrence:
    #         # from top: dfs(i-1, j)
    #         # from left: dfs(i, j-1)
    #         best_prev = min(dfs(i - 1, j), dfs(i, j - 1))

    #         memo[(i, j)] = grid[i][j] + best_prev
    #         return memo[(i, j)]

    #     return dfs(m - 1, n - 1)








        