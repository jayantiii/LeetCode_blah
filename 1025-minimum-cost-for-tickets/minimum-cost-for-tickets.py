class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * n  # dp[d] = min cost to cover up to day d  
        dp[0] = min(costs[0], costs[1], costs[2])

        for i in range(1,n):

            oneday =  dp[i-1] + costs[0]

            j = i-1
            while j >= 0 and days[j] > days[i] - 7: #condn --
                j-=1
            sevenday = dp[j] + costs[1] 

            while j >= 0 and days[j] > days[i] - 30:
                j-=1
            thirtyday = costs[2] + dp[j]

            dp[i] = min(oneday,sevenday,thirtyday)

        return dp[-1]

#---------- Recursion, works---------------------------------------
        # @lru_cache(None)
        # def mincost(i):
        #     if i == len(days):
        #         return 0

        #     oneday = costs[0] + mincost(i+1)

        #     j = i
        #     while j < len(days) and days[j] < days[i] + 7:
        #         j+=1
        #     sevenday = costs[1] + mincost(j)

        #     while j < len(days) and days[j] < days[i] + 30:
        #         j+=1
        #     thirtyday = costs[2] + mincost(j)

        #     return min(oneday,sevenday,thirtyday)

        # return mincost(0)

# With memo: O(n^2) time here (n states, each may scan forward up to n);
# O(n) space for cache + recursion stack.
# Without memo: exponential time (~3^n branching), O(n) recursion stack space.

#------------DP over all 365 days, better!!, 0(n)----------------------

        # travel = set(days)
        # dp = [0] * 366  # dp[d] = min cost to cover up to day d

        # for d in range(1, 366):
        #     if d not in travel:
        #         dp[d] = dp[d - 1]
        #     else:
        #         dp[d] = min(
        #             dp[d - 1] + costs[0],
        #             dp[max(0, d - 7)] + costs[1],
        #             dp[max(0, d - 30)] + costs[2],
        #         )
        # return dp[365]

        