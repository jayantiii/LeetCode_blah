# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #Understand every bit, backtracking --
        prefixsum = {0:1} 
        self.count = 0
        def dfs(node,currsum):
            if not node:
                return

            currsum = currsum + node.val
             # count paths ending at this node
            self.count += prefixsum.get(currsum - targetSum, 0) #just gets, doesnt create

            # add current prefix sum to the path
            prefixsum[currsum] = prefixsum.get(currsum, 0) + 1

            # recurse (DO NOT add node.val again)
            dfs(node.left, currsum)
            dfs(node.right, currsum)

            # backtrack
            prefixsum[currsum] -= 1 #IMP, undo the exact change

        dfs(root,0)

        return self.count
        

#use prefix sum and hashmap
# A downward path ending at current node sums to target if there exists an earlier prefix sum currSum - target.
# Keep a dict cnt[prefixSum] = how many times this prefix sum has appeared on the current root→node pat

#----------Mistakes-----------------------------------
# You can’t prune with (currSum + node.val) > targetSum because node values can be negative.

# You’re not using the prefix-sum idea correctly: you need a count map of prefix sums along the current root→node path, with backtracking.

#Prefixsum[target] is not the answer, prefixsum is only for current path, I coudlnt write the structure the on my own, confusing, Think!!

#-----------------Similar code---------------------------
        # prefixsum = {0: 1}.  #needed

        # def dfs(node, currsum):
        #     if not node:
        #         return 0

        #     currsum += node.val
        #     count = prefixsum.get(currsum - targetSum, 0)

        #     prefixsum[currsum] = prefixsum.get(currsum, 0) + 1
        #     count += dfs(node.left, currsum)
        #     count += dfs(node.right, currsum)
        #     prefixsum[currsum] -= 1  # backtrack

        #     return count

        # return dfs(root, 0)