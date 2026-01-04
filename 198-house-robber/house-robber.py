class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] is maxmoney can rob with 0...i houses
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1],nums[0])

        dp  = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) 
        for i in range(2,len(nums)):
            #skip
            dp[i] = max(dp[i], dp[i-1])

            #take
            dp[i] = max(dp[i], dp[i-2] + nums[i])

        return dp[len(nums)-1]

#---------------------Simpler,No Dp array, 2 vars-----------------------------
        # prev2 = 0  # dp[i-2]
        # prev1 = 0  # dp[i-1]

        # for x in nums:
        #     cur = max(prev1, prev2 + x)  # skip vs take
        #     prev2, prev1 = prev1, cur

        # return prev1

# ##----------Recursive--------------------------------------------       
#@lru_cache(maxsize=None)
#         def f(i: int) -> int:
#             if i >= n:
#                 return 0
#             skip = f(i + 1)
#             take = nums[i] + f(i + 2)
#             return max(skip, take)

#         return f(0)
