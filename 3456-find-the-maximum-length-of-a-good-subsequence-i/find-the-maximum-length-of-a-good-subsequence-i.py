class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ## 2D table: rows = index, cols = changes

        # length = [1 for i in range(k+1) for j in range(len(nums))] #see!

        # for i in range(len(nums)):
        #     for j in range(k+1):
        @cache
        def dfs(i, mismatch):
            if mismatch > k:
                return 0
            
            return 1 + max(
                (dfs(j, mismatch + (nums[i] != nums[j])) for j in range(i + 1, len(nums))),
                default=0)
        
        return max(dfs(i, 0) for i in range(len(nums)))





        
# In this problem, the state depends on two things: the number of changes k and the value of the last number.
#dp[i][j] = The maximum length of a subsequence ending exactly at index i using exactly j changes our budget is k

#  Identify the Two DimensionsAsk yourself: What are the two things changing that determine my current state?Dimension 1 (Rows): Usually the index of the array (progress through the data).Dimension 2 (Columns): Usually a constraint or limit (in this case, $k$ changes).

#Difficult to understand Q - it's asking for a sequence where there can only be k numbers that are not equal like 1, 2 and all the other number in the sequence must be the same. #dont forget line --> such that seq[i] != seq[i + 1].

# -----
# 2D DP$N \times K$"What's the best sequence ending at this specific index?"1D DP$K$ (plus map)"What's the best sequence ending in this value with $j$ changes?"


# -------------------------------- Bactrack soln, works-----------
#it give TLE without memo and MLE with memo ---- interesting
        # memo = {}
        # def maxlen(i,previ,k):#length of subsequence
        #     #Base
        #     if i == len(nums): 
        #         return 0  

        #     if (i,previ,k) in memo:
        #         return memo[(i,previ,k)]            

        #     #skip
        #     skip = maxlen(i+1,previ,k)

        #     #take
        #     take = 0 #define here cause its local
        #     if previ == -1:
        #         take = 1+ maxlen(i+1,i, k)
        #     elif nums[i] == nums[previ]:
        #         take = 1+ maxlen(i+1,i, k)
        #     elif k > 0: #THIS IMP HERE!
        #         take = 1+ maxlen(i+1,i, k-1)

        #     res = max(skip,take)
        #     memo[(i,previ,k)] = res
        #     return res

        # return maxlen(0,-1,k)

#-----Below are mistakes i did while building the above backtrack solution--------
# 1) i tried passing down length as function param
# - issue with how length is being passed down. In recursive optimization problems (like Longest Common Subsequence or Knapsack), you generally want the function to return the value found from that point forward, rather than carrying a running total down into the arguments.

#  Why carrying length is problematic:
# # If you carry length in the arguments, it makes memoization (caching) almost impossible. For the same index i and same k, the result could be different depending on what the length was when you reached it. This forces the computer to re-calculate the same sub-problems millions of times.

# 2) if k < 0: return 0 - I tried making this a base case, This shouldnt be a base case
#  -- k < 0 is an invalid state, not a natural end to a sequence; returning 0 would treat an illegal move as a successful valid path.
#so if u wanna do that u would rather return float('-inf') signifying invalid path

# -------------------------------------------------------------

# The first constraint nums.length <= 500 to remind you this problem can not be solved by backtracking
