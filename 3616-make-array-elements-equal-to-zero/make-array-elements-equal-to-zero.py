class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        #Difficult to come up, prefix sum!!!
        total = sum(nums)
        valid = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l = sum(nums[:i])
                r = sum(nums[i+1:])
                if l == r: valid+=2
                elif abs(l-r) == 1: valid+=1

        return valid

#For each index i where nums[i] == 0, let
# L = sum(nums[:i]) and R = sum(nums[i+1:]).
# if L == R → both directions work (add 2)
# if abs(L - R) == 1 → exactly one direction works (add 1)
# else → add 0
# Compute L for all i with a running prefix sum; R = total - prefix - nums[i].
#Picture the process as a ping-pong ball bouncing between two piles of stones:

#-----------------Intuition for prefix sum----------------------------------------------
# Think of the walk as a “token” that bounces: every time it hits a positive cell, it removes 1 from that side and flips direction. So the whole process is basically moving 1 unit of work from left to right (or right to left) each bounce until everything is gone.

# Starting at a zero i, the only thing that matters is how many total units exist on the left vs the right:

# If left sum = right sum, the bounces can perfectly “pair up” units across the zero, so you’ll finish no matter which way you start.

# If one side has exactly 1 extra unit, you must start toward the heavier side; the first hit “consumes” that extra and then the rest pairs up.

# If the difference is ≥ 2, you’ll get stuck leaving leftovers on the heavier side because each bounce can only fix the imbalance by at most 1.

# So the simulation collapses to comparing L and R for each zero.

#------------------------ Recursion Bruteforce TLE reason:-------------------------------
# roll() simulates ONE decrement per step (numscopy[curr] -= 1), so 1 recursive call per 1 unit removed.
# A single simulation therefore takes ~Theta(total) steps where total = sum(nums).
# We also copy the array per trial: Theta(n).
# We run 2 trials (left + right) for each zero index; if z = count of zeros:
# Total time ~= Theta(z * (total + n))  -> too large -> TLE.

#LEFT CAN BE -1, RIGHT CAN BE +1

        # n = len(nums)
        # valid = 0
       
       #   # You must return roll(...) in both recursive branches!! structure!
        # def roll(curr: int, direction: int) -> bool:
        #     # If we walked off the array, the simulation ends:
        #     # it's valid only if everything is zero now.
        #     if curr < 0 or curr >= n:
        #         return sum(numscopy) == 0

        #     if numscopy[curr] == 0:
        #         return roll(curr + direction, direction)

        #     # numscopy[curr] > 0
        #     numscopy[curr] -= 1
        #     direction *= -1
        #     return roll(curr + direction, direction). #IMPPP!!! like this structure

        # for i in range(n):
        #     if nums[i] == 0:
        #         # try left, #left, right both count seperately
        #         numscopy = nums.copy()
        #         if roll(i - 1, -1):
        #             valid += 1

        #         # try right
        #         numscopy = nums.copy()
        #         if roll(i + 1, 1):
        #             valid += 1

        # return valid

##----------------Works,Bruteforce without recursion------------------------------------------
# class Solution:
#     def simulate(self, nums: list[int], start: int, dir: int) -> bool:
#         n = len(nums)
#         a = nums.copy()
#         curr = start
#         while 0 <= curr < n:
#             if a[curr] == 0:
#                 curr += dir 
#             else:
#                 a[curr] -= 1  
#                 dir = -dir   
#                 curr += dir 
#         return all(v == 0 for v in a)

#     def countValidSelections(self, nums: list[int]) -> int:
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             if nums[i] != 0:
#                 continue
#             if self.simulate(nums, i, -1):
#                 ans += 1  
#             if self.simulate(nums, i, +1):
#                 ans += 1 
#         return ans
