class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        #I DIDNT WRITE THIS!
        n = len(values)
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            # vertices i..j
            # < 3 vertices => no triangle can be formed inside
            if j - i < 2:
                return 0

            best = float("inf")
            # pick middle vertex k to form triangle (i, k, j)
            for k in range(i + 1, j):
                best = min(
                    best,
                    dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
                )
            return best

        return dp(0, n - 1)

# Idea (Interval DP):

# dp(i, j) = minimum triangulation score for the polygon slice using vertices i..j (in order).
# If j - i < 2, there are < 3 vertices -> no triangle possible -> cost 0.
# Otherwise, choose a middle vertex k (i < k < j) to form triangle (i, k, j).
# That triangle splits the slice into two smaller slices: (i..k) and (k..j).
# So:
#   dp(i, j) = min over k in (i+1..j-1) of:
#              dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
# Answer = dp(0, n-1)


# from typing import List
# from functools import lru_cache

# class Solution:
#     # -------------------- 1) RECURSIVE (Top-down DP with memo) --------------------
#     def minScoreTriangulation_recursive(self, values: List[int]) -> int:
#         n = len(values)

#         @lru_cache(None)
#         def dp(i: int, j: int) -> int:
#             # vertices i..j
#             # < 3 vertices => no triangle can be formed inside
#             if j - i < 2:
#                 return 0

#             best = float("inf")
#             # pick middle vertex k to form triangle (i, k, j)
#             for k in range(i + 1, j):
#                 best = min(
#                     best,
#                     dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
#                 )
#             return best

#         return dp(0, n - 1)

#     # -------------------- 2) ITERATIVE DP (Bottom-up table) --------------------
#     def minScoreTriangulation(self, values: List[int]) -> int:
#         n = len(values)
#         dp = [[0] * n for _ in range(n)]

#         # length is interval size: j - i
#         # need at least 2 to have 3 vertices (i, i+1, i+2)
#         for length in range(2, n):
#             for i in range(0, n - length):
#                 j = i + length
#                 best = float("inf")
#                 for k in range(i + 1, j):
#                     best = min(
#                         best,
#                         dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
#                     )
#                 dp[i][j] = best

#         return dp[0][n - 1]

