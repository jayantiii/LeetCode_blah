class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])
        @lru_cache(None)
        def backtrack(i,j):
            if i < 0 or i >= m or j <0 or j >= i + 1: # cond j >= i + 1
                return 0

            first = backtrack(i+1, j)
            second = backtrack(i+1,j+1)

            return triangle[i][j] + min(first,second)

        return backtrack(0,0)
        