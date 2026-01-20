class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(i): #i is the position in string
            if i == len(s): #whole string found
                return True
            for word in wordDict:
                lenw = len(word)
                if i + lenw <= len(s) and word == s[i: i+lenw]:
                    if dfs(i+lenw): #return true dont forget
                        return True

            return False
        return dfs(0)

#IMP -> Each node will have len(wordDict) branches!
##--------DP-----------------------      
# dp[i] = True if the prefix s[:i] (first i characters)
#  can be split into dictionary words.

        # words = set(wordDict)
        # n = len(s)
        # max_len = max((len(w) for w in words), default=0)

        # dp = [False] * (n + 1)
        # dp[0] = True  # empty prefix is valid

        # for i in range(1, n + 1):
        #     # check splits ending at i: s[j:i]
        #     start = max(0, i - max_len)
        #     for j in range(start, i):
        #         if dp[j] and s[j:i] in words:
        #             dp[i] = True
        #             break

        # return dp[n]