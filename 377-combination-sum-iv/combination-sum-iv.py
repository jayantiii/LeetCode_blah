class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp[i] is number of possible combinations to add upto i
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] = dp[i] + dp[i-num] #possible ways

        return dp[target]
             

# Follow up: 
# What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

# Allowing negative numbers breaks the problem because you can create infinite sequences that still sum to the target.

# Example: nums = [1, -1], target = 1
# Valid sequences: [1], [1, -1, 1], [1, -1, 1, -1, 1], … infinitely many.
# So “number of combinations” is not well-defined (it diverges), and the DP recurrence dp[i] += dp[i-num] can’t terminate meaningfully.

# To allow negatives, you must add a limitation that prevents cycling / infinite length, e.g.:
# Limit the length of the sequence (e.g., “use at most L numbers”), then you can do DP by (sum, length). Then can do dp[len][sum] = #ways to make sum using exactly len numbers

# Or limit how many times each number can be used (bounded counts), turning it into a bounded knapsack-style counting problem.
# The standard clean fix is: add a maximum length L (or maximum number of elements).

#----------------------------Follow up soln--------------------------------
   # dp[t] = ways to make sum t using exactly current length `len`

   #IMPPP, ITS SPARSE DP
   #store dp as a hash map (dict): only sums that are actually reachable are kept (sparse DP).

        # dp = {0: 1}          # len = 0
        # ans = 0              # ways to make target using length <= L

        # for _len in range(1, L + 1):
        #     nxt = {}
        #     for s, cnt in dp.items():
        #         for x in nums:
        #             ns = s + x
        #             nxt[ns] = nxt.get(ns, 0) + cnt
        #     ans += nxt.get(target, 0)
        #     dp = nxt

        # return ans
