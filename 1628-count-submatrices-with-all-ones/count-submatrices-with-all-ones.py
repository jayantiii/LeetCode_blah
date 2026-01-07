class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        #Works but brute for kinda
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

        
##------------Most optimal O(m,n) solution----------------------------
#Clue path: turn each row into a histogram, then for each row count “all-ones submatrices ending at this row” using a monotonic increasing stack.

# m, n = len(mat), len(mat[0])
#         heights = [0] * n
#         total = 0
        
#         for i in range(m):
#             # Update heights for the current row (histogram heights)
#             for j in range(n):
#                 heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            
#             # Use a monotonic stack to count rectangles ending at row 'i'
#             # stack stores: (height, number of rectangles ending here)
#             stack = []
#             row_sum = 0
#             for j in range(n):
#                 count = 0
#                 # When we encounter a shorter height, we must "cap" the rectangles
#                 while stack and stack[-1][0] >= heights[j]:
#                     stack.pop()
                
#                 if not stack:
#                     # If no smaller height to the left, the width is (j + 1)
#                     count = heights[j] * (j + 1)
#                 else:
#                     # Width is limited by the previous smaller height's index
#                     prev_h, prev_count = stack[-1]
#                     # rectangles = (height * distance to prev smaller) + previous count
#                     count = heights[j] * (j - stack[-1][2]) + prev_count
                
#                 # We store height, the count of rectangles ending here, and current index
#                 stack.append((heights[j], count, j))
#                 row_sum += count
                
#             total += row_sum
            
#         return total

##--- Brute force without recursion--------------------------------------------
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
  