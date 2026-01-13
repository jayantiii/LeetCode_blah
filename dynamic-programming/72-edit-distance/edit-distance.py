class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0]* (n+1) for i in range(m+1)]

        # base cases
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):

                if word1[i-1] == word2[j-1]: #indexing
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #THESE 3, I found lil confuse at start!!
                    insert = dp[i][j - 1]  # insert into word1 to match word2[j-1]
                    delete = dp[i - 1][j]   # delete word1[i-1]
                    replace = dp[i - 1][j - 1] # replace word1[i-1] -> word2[j-1]
                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[m][n]


#----------------------------My mistakes----------------------------------
# 4) Transition is incomplete:
#    Edit distance needs 3 choices when chars differ:
#      insert  -> dp[i][j-1]
#      delete  -> dp[i-1][j]
#      replace -> dp[i-1][j-1]
#    You only use dp[i-1][j], so you're basically only counting deletions from word1.

# 5) Even the "match" case is wrong:
#    If chars match, it should be dp[i-1][j-1] (no new cost),
#    but you used dp[i-1][j], which changes the length mismatch and breaks the model.

#--------------------------- Recursive------------------------------
        # @lru_cache(None)
        # def f(i: int, j: int) -> int:
        #     # If one string is finished, only option is to insert/delete the rest
        #     if i == m:
        #         return n - j  # insert remaining chars of word2
        #     if j == n:
        #         return m - i  # delete remaining chars of word1

        #     # If chars match, move both
        #     if word1[i] == word2[j]:
        #         return f(i + 1, j + 1)

        #     # Else: try 3 operations
        #     insert = 1 + f(i, j + 1)      # insert word2[j] into word1
        #     delete = 1 + f(i + 1, j)      # delete word1[i]
        #     replace = 1 + f(i + 1, j + 1) # replace word1[i] -> word2[j]
        #     return min(insert, delete, replace)

        # return f(0, 0)








        