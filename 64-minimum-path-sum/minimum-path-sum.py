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








        