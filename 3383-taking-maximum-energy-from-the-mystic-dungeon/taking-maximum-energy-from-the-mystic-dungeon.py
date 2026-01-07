class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Let dp[i] denote the energy we gain starting from index i. 
        n = len(energy)
        dp = [energy[i] for i in range(n)]

        for i in range(n-k-1,-1,-1):
                dp[i] = dp[i+k] + energy[i]

        return max(dp)
        
# we need to find a optimal starting point

#---------------------------dfs--------------------------------------------
        # @lru_cache(None)
        # def dfs(i: int) -> int:
        #     if i >= n:
        #         return 0
        #     j = i + k
        #     return energy[i] + (dfs(j) if j < n else 0)

        # return max(dfs(i) for i in range(n))