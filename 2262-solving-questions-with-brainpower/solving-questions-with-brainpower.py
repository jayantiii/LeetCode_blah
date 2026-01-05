class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def backtrack(i):
            if i >= len(questions): #not ==, should be =>
                return 0

            #skip
            skip = backtrack(i+1)

            #take 
            brainpower = questions[i][1]
            take = questions[i][0] + backtrack(i + brainpower+1)

            return max(skip,take)

        return backtrack(0)

#---------------------------Bottom up Dp, suffix backward-----------------
        # n = len(questions)
        # dp = [0] * (n + 1)  # dp[i] = best from i..end

        # for i in range(n - 1, -1, -1):
        #     points, brainpower = questions[i]
        #     nxt = min(n, i + brainpower + 1)
        #     dp[i] = max(dp[i + 1], points + dp[nxt])

        # return dp[0]
    
#---------------------------Bottom up Dp, prefix forward-----------------
#  n = len(questions)
#         dp = [0] * (n + 1)  # dp[i] = best score upon reaching index i

#         for i in range(n):
#             # skip i
#             dp[i + 1] = max(dp[i + 1], dp[i])

#             # take i
#             points, brainpower = questions[i]
#             nxt = min(n, i + brainpower + 1)
#             dp[nxt] = max(dp[nxt], dp[i] + points)

#         return dp[n]  # dp is non-decreasing due to skip transitions

        