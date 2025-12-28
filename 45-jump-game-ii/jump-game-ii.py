class Solution:
    def jump(self, nums: List[int]) -> int:
#from a index u can jump few indices, from, those more#see pattern , looks like can do bfs
        #start from the goal
        end = 0
        farthest = 0
        jumps= 0
        goal = len(nums) -1
        for i in range(len(nums)-1):
            canjump = nums[i]
            farthest = max(farthest,i + canjump)
            if i == end:
                jumps+=1
                end = farthest
        return jumps

        
            

#forward loop is better for this problem




#the greedy solution is the real optimal O(n) method
# How to explain it in one breath
# Treat all indices reachable with jumps jumps as one BFS level [0..end].
# While scanning that level, compute farthest reach for the next jump.
# When you hit end, you must “take a jump” → jumps++, advance end=farthest.
#------------kinda like dp, works but tle on some cases, 0(n2)

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

        
        