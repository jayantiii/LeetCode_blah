class Solution:
    def jump(self, nums: List[int]) -> int:
# see pattern , looks like can do bfs types but in greedy way
        n = len(nums)
        if n <= 1:
            return 0

        end = 0
        farthest = 0
        jumps= 0
        for i in range(len(nums)-1):
            canjump = nums[i]
            farthest = max(farthest,i + canjump)
            if i == end:
                jumps+=1
                end = farthest
        return jumps

# end = farthest index reachable with current number of jumps
# farthest = farthest index reachable with one more jump
# When you hit end, you must take a jump → level increments.       

#forward loop is better for this problem rather than backward
# “Jump Game I” (can reach end?) works nicely backward because it’s a yes/no problem with a monotone invariant. “Jump Game II” (minimum jumps) is an optimization problem, and backward scanning loses the “single pass” property.
# If the problem is decision (True/False), a monotone invariant scan (often backward) may be O(n).
# If the problem is min/max number of steps, think BFS levels / greedy intervals / DP, because you’re optimizing over paths.

#-------------------

#the greedy solution is the real optimal O(n) method
# How to explain it in one breath
# Treat all indices reachable with jumps jumps as one BFS level [0..end].
# While scanning that level, compute farthest reach for the next jump.
# When you hit end, you must “take a jump” → jumps++, advance end=farthest.
#------------kinda like dp, works but tle on some cases, 0(n2)------------------------------------

        # res = [float('inf')]*len(nums) #store minimum jump to reach each index
        # res[0] = 0 #start pos
        # i = 0
        # while i<len(nums):
        #     jump = nums[i]
        #     for j in range(i + 1, min(len(nums), i + jump + 1)):
        #         res[j] = min(res[j], res[i] + 1)
        #     i += 1  # must move 1-by-1, not by jump length
        #     print(res)
        # return res[-1]

#-----------Neeetcode------------------------------
# def jump(nums):
#     n = len(nums)
#     res = 0
#     l = r = 0

#     while r < n - 1:
#         farthest = r
#         for i in range(l, r + 1):
#             farthest = max(farthest, i + nums[i])

#         if farthest == r:          # can't expand (only needed if end may be unreachable)
#             return -1

#         l = r + 1
#         r = farthest
#         res += 1

#     return res

        
        