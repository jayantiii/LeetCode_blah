# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node): # no need of maxvalue arg
            if not node:
                return 0
            if node in memo:
                return memo[node]
            #skip
            left = dfs(node.left)
            right = dfs(node.right)
            skip = left + right

            #Take
            take = node.val
            if node.left:
                take += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                take += dfs(node.right.left) + dfs(node.right.right)

            memo[node] = max(skip,take)

            return memo[node]


        return dfs(root)



# You can look at the tree in a top-down manner, there will be two cases
# max containing the root node
# max excluding the root and including the child nodes
# In a dfs manner, traverse the tree and for each root return these values as a pair.

# So for each node we have a pair containing the max value possible by including/excluding the particular node

##----- Imp to understand-----------
##-----------DP (dynamic programming) solution on a tree, Tree dp--------------
##===== dfs solution, without cache and time O(n)========================
        # def dfs(node):
        #     if not node:
        #         return (0, 0)  # (rob_this, not_rob_this)

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     rob_this = node.val + left[1] + right[1]
        #     not_rob_this = max(left) + max(right)

        #     return (rob_this, not_rob_this)

        # return max(dfs(root))

# So the concept is exactly skip/take, but now:
# Each node stores both values (rob_this, not_rob_this) → like a mini DP table for that node.
# We never recompute the same subtrees, unlike brute force.
# Bottom-up recursion automatically propagates results from children to parent.

#  Brute force: “Try robbing or skipping every node, recompute everything every time.”
# DP/tree-DP: “Compute rob/not_rob for each node once, then reuse it for parent computations.”