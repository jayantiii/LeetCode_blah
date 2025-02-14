class Solution:
    def climbStairs(self, n: int) -> int:
        dp =  [0]* (n+1) #n + 1
        if n == 1 or n == 2:
            return n
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] # its n and not n +1!!!


# # passed only half cases because of TLE , so use dp
#  if n == 1 or n ==2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2) # dont forget self.