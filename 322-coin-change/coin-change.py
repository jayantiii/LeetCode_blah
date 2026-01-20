class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    #Think of this problems has subproblems, DP, dp is lil bit like bruteforce too
    #We need to find def mincoins(m) where this returns mincoins for any m
    #Then we have base base mincoins(0) = 0

    #Bottom up approach, find mincoins  for all m from 0 .... amount

        dp = [float('inf')]* (amount+1) # amount + 1 because starts from 0
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                remaining = amount - c
                if remaining >=0:
                    dp[i] = min(dp[i],1+dp[i-c]) #its  i-c
        

        return -1 if dp[amount] == float('inf') else dp[amount]



# Bottom-up: iterative DP, O(A * N) time, O(A) space.
# Top-down: recursive + memo, same complexity, sometimes easier to think directly from the recurrence. Time: O(amount * len(coins)) Space: O(amount) (memo) + O(amount) (stack) → still O(amount)

#Brute Force Idea: Try every possible combination of coins and find the one with minimum coins that sums to the target amount.
#Greedy approach would be, pick the largest as much as you can , if not then go lower but fails in cases
# like [1,3,4,5] amt = 5 -> it will return 5,1,1


#---------Bottom up but reverse the loop order--------------------------

# INF = 10**9
# dp = [INF] * (amount + 1)
# dp[0] = 0

# for c in coins:
#     for i in range(c, amount + 1):   # increasing => can reuse coin c
#         dp[i] = min(dp[i], dp[i - c] + 1)

# Min/max DP(this): loop order doesn’t matter because min/max just picks the best value for each dp[i]—no double-counting.

# Counting DP(coin change 2): loop order matters because += accumulates paths; wrong order counts different orders separately (permutations vs combinations).
#----------------------------------Recursive---------------------------
    #  @lru_cache(None)
    #     def mincoins(rem: int) -> int:
    #         if rem == 0:
    #             return 0
    #         if rem < 0:
    #             return INF

    #         best = INF
    #         for c in coins:
    #             best = min(best, 1 + mincoins(rem - c))
    #         return best

    #     ans = mincoins(amount)
    #     return -1 if ans >= INF else ans

##DP explaination
# Recurrence:
#   solution(0) = 0
#   solution(m) = min_{c in coins} ( solution(m - c) ) + 1
#
# Recursion tree for solution(13):
#
#                               13
#                 /              |              \
#               -5              -4              -1
#           (use 5)         (use 4)         (use 1)
#
#                               13
#                 /                  \                  \
#              8 (13-5)            9 (13-4)            12 (13-1)
#
#
#     8 branch:                         9 branch:
#
#                     8                                 9
#             /         |         \              /         \
#       3 (8-5)     4 (8-4)     7 (8-1)     4 (9-5)      5 (9-4)



