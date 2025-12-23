class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ##dp[i][j] represents the length of the common subarray ending exactly at those indices. - prefix way!
        dp = [[0] * (len(nums1) + 1 ) for j in range(len(nums2)+1)]
        maxlength = 0
        for i in range(1,len(nums2)+1): #rows
            for j in range(1,len(nums1)+1): #cols
                if nums1[j-1] == nums2[i-1]: # imp to see why we use -1
                    dp[i][j] = 1 + dp[i-1][j-1]
                maxlength = max(maxlength,dp[i][j])
                #dp[i][j] remains 0 because the "streak" is broken
              

        return maxlength

 
# Note - There can be different ways to define d[i][j] and based on that code can differe, dont mix up eevrything. See below to understand    

#------ Second DP way ------------------------
#streak[i][j]: The length of the match ending exactly at this spot (crucial for subarrays).
#dp[i][j]: The "Global Max" seen anywhere in the ixj rectangle of the grid.

    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     n, m = len(nums1), len(nums2)
        
    #     # 'streak' tracks the contiguous match ending at (i, j)
    #     streak = [[0] * (m + 1) for _ in range(n + 1)]
        
    #     # 'dp' tracks the maximum streak found anywhere in the rectangle (0,0) to (i,j)
    #     dp = [[0] * (m + 1) for _ in range(n + 1)]
        
    #     for i in range(1, n + 1):
    #         for j in range(1, m + 1):
    #             # 1. Calculate the local streak (must be contiguous)
    #             if nums1[i-1] == nums2[j-1]:
    #                 streak[i][j] = 1 + streak[i-1][j-1]
    #             else:
    #                 streak[i][j] = 0 # Streak breaks if elements don't match
                
    #             # 2. Update the cumulative maximum for this sub-grid
    #             # We look at the max above, the max to the left, and the current streak
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1], streak[i][j])
        
    #     # The final answer is the record held in the very last cell
    #     return dp[n][m]

# ----------------------- Third DP WAY - suffix way---------------
# dp[i][j] will be the longest common prefix of A[i:] and B[j:]. suffix way
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         n, m = len(nums1), len(nums2)
#         # Table size (n+1)x(m+1) to handle the i+1, j+1 boundary
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
#         max_len = 0
        
#         # Outer loops go BACKWARD (end to start)
#         for i in range(n - 1, -1, -1):
#             for j in range(m - 1, -1, -1):
#                 if nums1[i] == nums2[j]:
#                     # Look FORWARD at the next diagonal
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                     max_len = max(max_len, dp[i][j])
#         return max_len

#------------MY MISTAKES WHILE WRITING DP CODE -------------
#1)# else: --- # dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# -- I write the above condition, but this wrong, if it dont match, it should start from zero

 #2)##handle first row and col
                # if i== 0 or j == 0:
                #         dp[i][j] = 1 if nums1[j] == nums2[i] else 0
                #         continue

# -- I tried handling like this but this can be problematic, better apporach is to
# --  dp = [[0] * (len(nums1) + 1 ) for j in range(len(nums2)+1)]
# -- initliase like this so that there is a extra start row and col

# 3) return dp[i-1][j-1] , this is not the answer

# -----------------------------Bruetforce ------------------------------
#Bruet force apporach - just copy pasted it here!
#max_len = 0
        # n, m = len(nums1), len(nums2)
        
        # # 1. Start at every possible index in nums1
        # for i in range(n):
        #     # 2. Start at every possible index in nums2
        #     for j in range(m):
                
        #         # 3. Match elements one by one starting from (i, j)
        #         k = 0
        #         while (i + k < n) and (j + k < m) and (nums1[i + k] == nums2[j + k]):
        #             k += 1
                
        #         # 4. Update the global maximum length
        #         max_len = max(max_len, k)
                
        # return max_len