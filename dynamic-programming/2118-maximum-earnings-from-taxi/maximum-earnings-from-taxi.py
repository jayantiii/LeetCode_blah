class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
 # dp[i] = best earnings ending at ith ride (rides[0..i-1]), Time: O(m log m), Space: O(m)

        rides.sort(key=lambda x: x[1])
        m = len(rides)
        if m == 0:return 0
        ends = [e for _, e, _ in rides]
        dp = [0] * m        # dp[i] = best earnings ending at ride i (take i)
        pref = [0] * m      # pref[i] = max(dp[0..i])

        for i, (s, e, tip) in enumerate(rides):
            profit = (e - s) + tip

            # compatible rides are those with end <= s -> indices [0..j-1]
            j = bisect_right(ends, s) #understand!
            best_prev = pref[j - 1] if j > 0 else 0

            dp[i] = best_prev + profit
            pref[i] = max(pref[i - 1], dp[i]) if i > 0 else dp[i]

        return pref[-1]   # same as max(dp)
  

#--------- Bucket based dp soln, No sorting , IMP, Time: O(n + m), Space: O(n + m) --------------------------------
#dp[x]=maximum money you can have when you reach point x
# # end_at[e] = list of rides that end at point e also buckets , Store each as (s, profit) in that bucket
# You didn’t finish a ride at x ⇒ you just came from x-1 ⇒ dp[x-1]
# You finished a ride at x ⇒ it started at some s ⇒ money = dp[s] + profit
#we sweep the road once, and at each point x we update dp[x] using only rides that end at x, because that’s the only moment they can increase earnings.

        # end_at = [[] for _ in range(n + 1)]
        # for s, e, tip in rides:
        #     end_at[e].append((s, (e - s) + tip))

        # dp = [0] * (n + 1)
        # for x in range(1, n + 1):
        #     dp[x] = dp[x - 1]  # move empty
        #     for s, profit in end_at[x]:
        #         dp[x] = max(dp[x], dp[s] + profit)

        # return dp[n]


#----------------Dp solution!! with different dp[i] definition  ----------------------------------------
#------ # dp[i] = best earnings considering first i rides (rides[0..i-1])
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

##------ same prev soln optimised with binary search , Time: O(m log m)
 #Because ends are sorted, those compatible rides form a prefix → find the cutoff  with binary search
        # rides.sort(key=lambda x: x[1])
        # ends = [e for _, e, _ in rides]
        # m = len(rides)

        # dp = [0] * (m + 1)  # dp[i] best considering first i rides
        # for i in range(1, m + 1):
        #     s, e, tip = rides[i - 1]
        #     profit = (e - s) + tip
        #     j = bisect_right(ends, s)
        #     dp[i] = max(dp[i - 1], dp[j] + profit)
        # return dp[m]

#--------------  Recursion soln, Time: O(m log m), Sp: O(m) [cache O(m) , stack up to O(m)]--------------------
        # @lru_cache(None)
        # def dp(index):
        #     if index == n:
        #         return 0

        #     s, e, t = rides[index]

        #     # not pick current passenger
        #     ans = dp(index+1)

        #     # pick current passenger, next available will be starting from j
        #     j = bisect_left(rides, [e,0,0])
        #     ans = max(ans, e-s+t+dp(j))

        #     return ans

        # n = len(rides)

        # return dp(0)

# -----------------------------------Longest Path in DAG Graph soln, Time: O(n + m) ---------------------
#  Our goal is to set the problem as a graph question. The graph will be a DAG, and as a result we can efficiently calculate the longest weighted path. When visiting a point, we update its neighbors to have the maximum possible earnings upon reaching that point.
#Nodes are road points 1..n, Each ride is a directed edge start -> end with weight as profit
#Because start < end and you only move forward, edges always go to a bigger node ⇒ DA
#dynamic programming on a DAG (longest path in a DAG), implemented as edge relaxation in topological order.

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

#----- Why sort by end and not start --------------------------------

# If you sort by start, the prefix 0..p can contain rides that start early but end very late.
# So even if rides[p].end ≤ s_i, the value dp[p] might come from some other ride k ≤ p that ends after s_i.
# Then dp[p] + profit_i chains an overlapping schedule (illegal), but your DP can’t see it because it only stored a number, not the actual last end time.

# You’re checking compatibility against one ride (p), but you’re adding profit on top of a value (dp[p]) that may come from a different ride inside that prefix.

#That’s the core reason: with start-sorting, dp[p] doesn’t imply “ends by s_i.”


#-----------How to understand that its Dp----------------------

# Think of it as: you’re choosing non-overlapping intervals (rides) to maximize total profit. That mental model tells you the “direction” immediately.

# “Pick some intervals, no overlaps, maximize sum.”
# = Weighted Interval Scheduling.

# When you have intervals, you want a DP state that represents:
# “Best money you can have earned up to some point.”

#---------------For intervals, when use dp and when just greedy ?----------------
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

# Read this - https://leetcode.com/problems/maximum-profit-in-job-scheduling/editorial/

  
