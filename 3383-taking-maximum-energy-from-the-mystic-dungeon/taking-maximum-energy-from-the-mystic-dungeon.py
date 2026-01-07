class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Let dp[i] denote the energy we gain starting from index i. 
        n = len(energy)
        dp = [energy[i] for i in range(n)]

        for i in range(n-k-1,-1,-1):
                dp[i] = dp[i+k] + energy[i]

        return max(dp)
        
# we need to find a optimal starting point