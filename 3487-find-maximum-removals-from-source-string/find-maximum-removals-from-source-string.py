class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        #dp[i][j] = minimum number of indices from targetIndices used to match pattern
        p = len(pattern)
        s = len(source)
        targetIndices = set(targetIndices)
        dp = [[float("inf")]* (p+1) for i in range(s+1)]

        # base: empty pattern costs 0 for any source prefix
        for i in range(s+1): #source
            dp[i][0] = 0
            for j in range(1,p+1): #pattern, start from 1
                # skip source[i-1]
                skip = dp[i - 1][j]

                #Take
                take = float("inf")
                if source[i-1] == pattern[j-1]:
                    if (i-1) in targetIndices: #Imp -> check i-1
                        take = dp[i-1][j-1] + 1 # or use cost variable
                    else:
                        take = dp[i-1][j-1] + 0
            
                dp[i][j] = min(dp[i][j],skip,take)

        return len(targetIndices) - dp[s][p] 
# pattern
#    a b a
# a  i
# b.    b
# b
# a
# a

#maxop = size(targetindices) - (number of common indices in targetindices and choosen subsequence)
# helpful to frame the problem the other way round, that is, what's the minimum number of targetIndices to use to build a subsequence pattern out of source?

# There are many ways to realize pattern as a subsequence of source (many “embeddings”). Every time your chosen embedding uses an index that lies in targetIndices, that index becomes protected (can’t be removed). So you want an embedding that uses as few targetIndices positions as possible.

# Because there are many subsequence “embeddings” of pattern in source, and a choice that looks good locally (e.g., “pick the earliest match” or “avoid targetIndices when possible”) can force you into using more targetIndices later. Any purely greedy rule will have counterexamples.
#So you need a method that considers future consequences. That’s exactly what DP is doing here

##---------------------------------------- Backtracking-------------------------
        # maxop = 0
        # p = len(pattern)
        # s = len(source)
        # targetIndices = set(targetIndices)

        # @lru_cache(None) #syntax
        # def backtrack(i,j):
        #     if j == p: #subsequence complete
        #         return 0 
        #     if i== s: # source exhausted but pattern remains
        #         return float("inf") #return inf, not zero!

        #     #skip
        #     skip = backtrack(i+1,j)

        #     #take
        #     cost= 0 
        #     if source[i] == pattern[j]:
        #         cost = 1 if i in targetIndices else 0
        #         take = backtrack(i+1,j+1)

        #         return min(skip, cost + take) #return statment

        #     return skip  # <- missing before!!
        #     #return min(skip, take), or do this and add take = float("inf") before if condn

        # minimum= backtrack(0,0)  #i is of source, j is of pattern
        # return len(targetIndices) - minimum

# dp[i][j] is defined on PREFIXES:
#   i = number of chars taken from source -> source[:i]
#   j = number of chars matched from pattern -> pattern[:j]
#
# Prefixes include the empty prefix:
#   source[:0]  (use 0 chars)
#   pattern[:0] (match 0 chars)
#
# Therefore:
#   i ranges 0..s  -> need (s + 1) rows
#   j ranges 0..p  -> need (p + 1) cols

        