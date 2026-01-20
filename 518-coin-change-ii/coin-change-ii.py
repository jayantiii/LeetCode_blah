class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #DP, fill ways to make amount of 1....amount
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:                       # coin outer => combinations
            for i in range(c, amount + 1):    # increasing => infinite use
                dp[i] += dp[i - c]

        return dp[amount]

#----------------If inifinte use not allowed----------------------
    #  for c in coins:                      # each coin considered once
    #         for a in range(amount, c - 1, -1):  # DESC => prevents reuse
    #             dp[a] += dp[a - c]

    #     return dp[amount]


# Meaning: the number of ordered sequences of coins that sum to i, where each coin can be used unlimited times. But Coin Change II (518) wants combinations where order doesn’t matter:

    #       for i in range(amount+1):
    #         for c in coins:
    #             amountremain = i -c
    #             if amountremain >= 0:
    #                 dp[i] += dp[amountremain]

    #     return dp[-1]

#DFS WITH FOR LOOP PATTERN   
        # numways = 0
        # memo = {}
        # def coinsdfs(i,amountremain):
        #     if (i,amountremain) in memo:
        #         return memo[(i,amountremain)]
        #     if amountremain == 0:
        #         return 1
        #     if amountremain < 0:
        #         return 0

        #     ways = 0
        #     for j in range(i,len(coins)):
        #         ways+=coinsdfs(j, amountremain - coins[j])
        #     memo[(i,amountremain)] = ways
        #     return ways

        # return coinsdfs(0,amount)

#DFS WITHOUT FOR LOOP PATTERN   
# def dfs(i: int, remain: int) -> int:
#             # If exact amount formed
#             if remain == 0:
#                 return 1
#             # If coins exhausted or overshoot
#             if i == len(coins) or remain < 0:
#                 return 0

#             # Choice 1: take the i-th coin (stay on same index)
#             take = dfs(i, remain - coins[i])

#             # Choice 2: skip the i-th coin (move to next index)
#             skip = dfs(i + 1, remain)

#             return take + skip

#         return dfs(0, amount)

# i = which coin types are still allowed - thus we need to pass it
# remain = how much money is left to form
#we need combinations, not permutations