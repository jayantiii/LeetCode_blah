class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
#dp[i] -> longest chain ending at pair i || O(n2)
        pairs.sort(key = lambda x:x[1])
        n  = len(pairs)
        dp = [1]*n
        for i in range(n):
            for j in range(i): #check all previous values
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        # Wrong -return dp[n-1] #  “best chain ending at last pair,” not the global best.


#------------ Greedy way - 0(nlogn) , best soln ---------------p
#   if not pairs: return 0
#         #sort accord to right pair
#         pairs.sort(key = lambda x:x[1])
#         maxlongest = 1

#         currend = pairs[0][1]
#         for i in range(1,len(pairs)):
#             if currend < pairs[i][0]:
#                 maxlongest +=1
#                 currend = pairs[i][1]

#         return maxlongest

# ------ My MISTAKE while writing greedy----------------------
# 1)if pairs[i-1][1] < pairs[i][0]: -- wrong to check previous, we need currend
#2) i tried doing maxlongest, currlongest,   maxlongest = max(currlongest,maxlongest)

# This all was wrong and not needed - In the correct greedy solution, the chain length only ever increases when you accept a pair, so currlongest and all is not needed

#------My mistake while writing DP-------------------
#1) I tried defining dp like # best[i] = best chain using pairs[0..i]
# --- wrong and does not tell you what the last end is. So you can’t safely extend it.
# That’s why the correct 1D state is:
# dp_end[i] = best chain length that ends exactly at pair i


#----- make dp soln from O(n2) to 0(nlogn) by using binary search-----------
#------DP with binary search O(nlogn)-------------------------

# After sorting pairs by end, the ends array is sorted.
# For a given start = s, the pairs that can come before it are exactly those with end < s.
# In a sorted list, all values < s form a prefix, so we can find the prefix boundary with binary search in O(log n).

    #    pairs.sort(key=lambda p: p[1])  # sort by end

    #     ends = []        # ends[i] = pairs[i].end
    #     pref = []        # pref[i] = best chain length among pairs[0..i]
    #     best = 0

    #     for s, e in pairs:
    #         k = bisect_left(ends, s) - 1      # last index with end < s
    #         prev_best = pref[k] if k >= 0 else 0
    #         curr = prev_best + 1

    #         best = max(best, curr)
    #         ends.append(e)
    #         pref.append(best)

    #     return best

