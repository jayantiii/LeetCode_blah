class Solution:
    def numTrees(self, n: int) -> int:
        #Let dp[n] = number of unique BSTs you can build with n distinct values.
        dp = [0]*(n+1) # 1based indexing
        # Empty tree is 1 way (important for when left or right subtree has 0 nodes).
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            #Find dp[i] by considering each 0,1,..i as root and adding their dps
            for root in range(1,i+1): #0..i
                leftree = dp[root-1]
                rightree = dp[i-root]
                total = leftree *rightree # Multiply! cause combinations
                dp[i] = dp[i] + total
        return dp[n]

# # left subtree size  = i - 1
# # right subtree size = n - i
# # Now the key insight:
# # The number of possible left subtrees = dp[i-1]
# # The number of possible right subtrees = dp[n-i]
# We only care about count, not actual tree shapes.

#  Key idea:
#         ----------
#         - For a fixed total size k, try every value as the ROOT.
#         - Suppose we choose value 'root' as the root (1..k):
#               left subtree size  = root - 1
#               right subtree size = k - root
#           Number of trees with this root =
#               (number of ways to build left subtree)  *
#               (number of ways to build right subtree)
#             = dp[left_size] * dp[right_size]
#         - Sum this over all choices of root.

#         Recurrence:
#         -----------
#             dp[k] = sum_{root=1..k} dp[root-1] * dp[k-root]

#         Base case:
#         ----------
#         - dp[0] = 1  (there is exactly ONE empty tree shape)
#         - dp[1] = 1  (single node tree)

#Why dp[L] * dp[R]?
# If you have A ways to pick X, and B ways to pick Y, and you must choose both X and Y,
# then total ways = A * B. 

#--------Why DP?---------------------------
# Whenever a question asks “how many ways…?” rather than “build all trees”, it often smells like DP or combinatorics.
# Overlapping subproblems
# You keep computing:
# number of BSTs with 1 node
# number of BSTs with 2 nodes
# number of BSTs with 3 nodes
# again and again if you brute-force → classic DP hint.
# So:
# counting + smaller repeatable subproblems = DP.