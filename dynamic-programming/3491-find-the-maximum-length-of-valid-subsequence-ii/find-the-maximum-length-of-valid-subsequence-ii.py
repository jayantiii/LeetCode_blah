class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        #dp[i][j] - #valid subs ending at i with modans be j
        dp = [[1]*k for i in range(len(nums))] 
        for i in range(1,len(nums)):
            for j in range(i):
                modans = (nums[j] + nums[i]) % k
                dp[i][modans] = max(dp[i][modans], dp[j][modans] + 1)

        return max(max(row) for row in dp)



            




# # Modular addition: (a + b) % k == ((a % k) + (b % k)) % k
#-----------Mymistake--------------
# This below 1d dp i defined wont work!!
#dp[i] , longest valid subsequence ending at i 
# You don’t know in advance which remainder-pair pattern 
# (p,q) the optimal valid subsequence will follow, so dp[i] alone can’t capture it.

# The DP “grid” you actually need is k×k (pairs of remainders), not n×k.