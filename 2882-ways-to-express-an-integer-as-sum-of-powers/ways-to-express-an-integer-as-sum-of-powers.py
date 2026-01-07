class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        #i is where we try all values 1,2.... till i**x <= n
        def recursion(i,n):
            if i**x > n:
                return 0
            if i**x == n:
                return 1

            #skip i
            skip = recursion(i+1,n)

            #take i
            take = recursion(i+1,n - (i**x))

            return skip+ take

        return recursion(1,n) %MOD
  

# If you iterate s increasing, then dp[s-p] may have already been updated earlier in the same loop for this same p, meaning it already includes solutions that used p. Then you add p again → you accidentally allow using p multiple times (that’s unbounded knapsack behavior).    

# Why backward fixes it
# If you iterate s downward, then when computing dp[s], the value dp[s-p] is at a smaller index, and it has not been updated yet in this iteration (because you haven’t reached it). So dp[s-p] still represents “ways without using p”, which is exactly what you want for 0/1 (unique) usage.
# That’s the whole rule of thumb:
# Forward sums ⇒ allows reuse of the same item (unbounded knapsack / coin change).
# Backward sums ⇒ each item used at most once (0/1 knapsack / unique set counting).

      # like 0/1 knapsnack problem
        ## dp[s] = #ways to make sum s using processed powers (each at most once)
        # dp = [0]*(n+1)

        # for i in range(n):
        #     for i in rage(n):