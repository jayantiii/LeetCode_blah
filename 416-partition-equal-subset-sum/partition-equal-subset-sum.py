class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numssum = sum(nums)
        if numssum % 2 !=0 :return False
        target = numssum //2

        dp = [False]*(target+1) #sum that are possible
        dp[0] = True 

        for i in range(len(nums)):
#backward cause - you update large sums first → they only see the old smaller sums, so x is used once.
            for s in range(target,nums[i]-1,-1): #stop at this so s >= x so (s-x) is valid
                if dp[s-nums[i]]:
                    dp[s] = True #this 
                if dp[target]:
                    return True

        return False    


#Observations
# Little hint. The subset sum can only be the total sum divided by two.
#If the sum of the nums are odd what does that mean? - then false
#If one subset is equal to the target number what does that mean about the rest of the numbers?
#How can we use dynamic programming to solve this problem?
# Make a bool[ ] with length of target + 1 which will store all the sums that are possible so far.#
#if possible[i] is true then possible[i + num] should also be true


#----Things that confused me while coding ------------
# Why two loops
# Outer loop over numbers x: process each item once.
# Inner loop over sums s: update which sums become reachable because of this x.

#IMPPPP -- Inner loop should go backwards and not forntwards
# Because forward iteration would let you use the same number x multiple times in the same pass, which turns the problem into a different one (unbounded knapsack). So forward uses “new dp” values again in the same pass → multiple uses of x.
# Backward fixes it because it prevents the current number x from “infecting” smaller sums and then being reused again immediately. Meaning: to make sum s using x once, you must have been able to make s-x before processing x.
# Forward = can reuse item many times (unbounded).
# Backward = use each item once (0/1).

# Sorting doesn’t really help here. This problem is a subset-sum decision problem: you need to know whether some subset sums to total/2. Ordering the numbers won’t change which sums are achievable.

#------------DFS soln----------------------------------

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total % 2:
#             return False
#         target = total // 2
#         nums.sort(reverse=True)

#         @lru_cache(None)
#         def dfs(i: int, s: int) -> bool:
#             if s == target:
#                 return True
#             if s > target or i == len(nums):
#                 return False
#             return dfs(i + 1, s + nums[i]) or dfs(i + 1, s)   #take or skip

#         return dfs(0, 0)

# Time: O(n * target)
# Space: O(n * target) for the cache (plus recursion depth O(n))

# Without memoization
# It branches include/exclude each number:
# Time: O(2^n) (worst case)
# Space: O(n) recursion stack