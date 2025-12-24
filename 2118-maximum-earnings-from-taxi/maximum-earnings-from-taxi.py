class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
 # dp[i] = best earnings ending at ith ride (rides[0..i-1])
        end_at = [[] for _ in range(n + 1)]
        for s, e, tip in rides:
            end_at[e].append((s, e - s + tip))

        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            dp[x] = dp[x - 1]  # move forward empty
            for s, profit in end_at[x]:
                dp[x] = max(dp[x], dp[s] + profit)

        return dp[n]
  
        
# Read this - https://leetcode.com/problems/maximum-profit-in-job-scheduling/editorial/

#----- Why sort by end and not start --------------------------

# If you sort by start, the prefix 0..p can contain rides that start early but end very late.
# So even if rides[p].end ≤ s_i, the value dp[p] might come from some other ride k ≤ p that ends after s_i.
# Then dp[p] + profit_i chains an overlapping schedule (illegal), but your DP can’t see it because it only stored a number, not the actual last end time.

# You’re checking compatibility against one ride (p), but you’re adding profit on top of a value (dp[p]) that may come from a different ride inside that prefix.

#That’s the core reason: with start-sorting, dp[p] doesn’t imply “ends by s_i.”


#-----------How to understand that its Dp-------------------

# Think of it as: you’re choosing non-overlapping intervals (rides) to maximize total profit. That mental model tells you the “direction” immediately.

# “Pick some intervals, no overlaps, maximize sum.”
# = Weighted Interval Scheduling.

# When you have intervals, you want a DP state that represents:
# “Best money you can have earned up to some point.”

#---------------For intervals, when use dp and when just greedy ?---------
# 1) Unweighted interval scheduling (classic greedy)
# Goal: pick the maximum number of non-overlapping intervals (every interval worth 1).
# Greedy works (sort by earliest end time, keep taking what fits) because of an exchange property:
# If you take the interval that ends earliest, you leave the most room for the rest.
# So local choice → global optimal. 

# 2) Weighted interval scheduling (this problem) - use dp
# Goal: pick non-overlapping intervals to maximize total weight/profit.
# Greedy generally fails because the exchange property breaks:
# An interval that ends early might have tiny weight.
# A longer interval might block multiple small ones, but still be worth it (or not).

#----------------Dp solution!! with different dp[i] definition  ----------------------------------------
 # dp[i] = best earnings considering first i rides (rides[0..i-1])
    #     rides.sort(key = lambda x:x[1])
        
    #     dp = [0 for i in range(len(rides))]
    #     dp[0] = rides[0][1] - rides[0][0] + rides[0][2]
    #     for i in range(1,len(rides)):
    #         # Option 1: skip ride i
    #         dp[i] = dp[i - 1]

    #  # Option 2: take ride i, chain with some j < i that ends <= s_i
    #         profit = rides[i][1] - rides[i][0] + rides[i][2]
    #         # p = last index < i with rides[p].end <= start2
    #         p = -1
    #         for j in range(i-1,-1,-1):
    #             end1 = rides[j][1]
    #             start2 = rides[i][0]
    #             if start2 >= end1: #not overlapping
    #                 p = j #index
    #                 break

    #         prev = dp[p] if p!= -1 else 0    
    #         dp[i] = max(dp[i], prev + profit)
    #     return dp[-1]

# -----------------------------------Longest Path in DAG Graph soln -------------
#  Our goal is to set the problem as a graph question. The graph will be a DAG, and as a result we can efficiently calculate the longest weighted path. When visiting a point, we update its neighbors to have the maximum possible earnings upon reaching that point.

        # g = defaultdict(list)
        # for start, end, tip in rides:
        #     g[start].append((end, end - start + tip))
        # profit = defaultdict(int)
        # prev_best = 0
        # for u in range(1, n + 1):
        #     prev_best = max(prev_best, profit[u])
        #     profit[u] = prev_best
        #     for v, w in g[u]:
        #         profit[v] = max(profit[v], profit[u] + w)
        # return prev_best  
  
