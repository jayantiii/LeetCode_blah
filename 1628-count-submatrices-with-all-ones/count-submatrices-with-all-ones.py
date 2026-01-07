class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        # right[r][c] = consecutive 1s to the right from (r,c)
        right = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n - 1, -1, -1):
                right[r][c] = 1 + right[r][c + 1] if mat[r][c] == 1 else 0

        def dfs_top_left(i: int, j: int, r: int, minw: int) -> int:
            # extend downward from row r, keeping min width so far
            if r >= m or right[r][j] == 0:
                return 0
            minw = min(minw, right[r][j])
            # minw rectangles end at row r (varying width 1..minw)
            return minw + dfs_top_left(i, j, r + 1, minw)

        total = 0
        INF = 10**9
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    total += dfs_top_left(i, j, i, INF)

        return total

        

#Clue path: turn each row into a histogram, then for each row count “all-ones submatrices ending at this row” using a monotonic increasing stack.

# class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         m, n = len(mat), len(mat[0])
#         res = 0
        
#         # Step 1: Pre-calculate consecutive 1s to the right for each cell
#         # row_sum[i][j] stores how many 1s are in mat[i][j:] consecutively
#         row_sum = [[0] * n for _ in range(m)]
#         for i in range(m):
#             count = 0
#             for j in range(n - 1, -1, -1):
#                 if mat[i][j] == 1:
#                     count += 1
#                 else:
#                     count = 0
#                 row_sum[i][j] = count
        
#         # Step 2: For each cell (i, j), count rectangles starting there
#         for i in range(m):
#             for j in range(n):
#                 # max_width tracks the narrowest row we've seen so far as we go down
#                 max_width = float('inf')
#                 for k in range(i, m):
#                     max_width = min(max_width, row_sum[k][j])
#                     res += max_width
#                     if max_width == 0: # Optimization: break if we hit a 0
#                         break
#         return res

#
        # m, n = len(mat), len(mat[0])

        # # right[r][c] = consecutive 1s to the right from (r,c)
        # right = [[0] * (n + 1) for _ in range(m)]
        # for r in range(m):
        #     for c in range(n - 1, -1, -1):
        #         right[r][c] = 1 + right[r][c + 1] if mat[r][c] == 1 else 0

        # def dfs_top_left(i: int, j: int, r: int, minw: int) -> int:
        #     # extend downward from row r, keeping min width so far
        #     if r >= m or right[r][j] == 0:
        #         return 0
        #     minw = min(minw, right[r][j])
        #     # minw rectangles end at row r (varying width 1..minw)
        #     return minw + dfs_top_left(i, j, r + 1, minw)

        # total = 0
        # INF = 10**9
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 1:
        #             total += dfs_top_left(i, j, i, INF)

        # return total

