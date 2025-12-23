class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # 'streak' tracks the contiguous match ending at (i, j)
        streak = [[0] * (m + 1) for _ in range(n + 1)]
        
        # 'dp' tracks the maximum streak found anywhere in the rectangle (0,0) to (i,j)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 1. Calculate the local streak (must be contiguous)
                if nums1[i-1] == nums2[j-1]:
                    streak[i][j] = 1 + streak[i-1][j-1]
                else:
                    streak[i][j] = 0 # Streak breaks if elements don't match
                
                # 2. Update the cumulative maximum for this sub-grid
                # We look at the max above, the max to the left, and the current streak
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], streak[i][j])
        
        # The final answer is the record held in the very last cell
        return dp[n][m]