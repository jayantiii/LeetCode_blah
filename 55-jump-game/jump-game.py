class Solution:
    def canJump(self, nums: List[int]) -> bool:
#A greedy solution, or greedy algorithm, is an algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding a global optimum.  

# Idea is to start from the end(goal) and keep updating the goal until we reach index 0

        res = False
        goal = len(nums) - 1 # last index
        for i in range(len(nums)-2, -1, -1):  
            #condition - i + nums[i] >= goal then
            if i + nums[i] >= goal:
                goal = i
        if goal == 0: res = True
        return res

        



#Brute force is - n to power n
# Brute force is from each position try every possible path
# if you cache it, can make it n2 but needed lil extra mem

# Idea is to track the farthest position can reach from any point