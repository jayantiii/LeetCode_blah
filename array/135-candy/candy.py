class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        #left to rigt, left neighbour
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1

        #right to left, right neighbour
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] >ratings[i+1]:
                candies[i] = max(candies[i], candies[i + 1] + 1) #max needed
        return sum(candies)
            

#In the right-to-left pass you must use max(...) so you don’t overwrite a bigger value set by the left-to-right pass.

#--------Further Space optimisation---------
# You can do it without the candies[] array by counting lengths of increasing/decreasing runs (“mountains”). This is still O(n) time, but harder to implement and explain.

# High-level:
# Track up = length of current increasing slope
# Track down = length of current decreasing slope
# Track peak = last up value to handle peak correction
# Accumulate candies as you go
# This is a known advanced variant; good if interviewer asks “can you do it in O(1) space?”

# The O(1)-space idea is: you don’t need candies[i] for every child, you only need the shape of the ratings as you scan: increasing runs, decreasing runs, and how tall the last peak was.

# --------------Intuition (before coding): -----------------------------------------
# - Everyone must get at least 1 candy.
# - Constraints are local:
#     if rating[i] > rating[i-1]  => candy[i] > candy[i-1]
#     if rating[i] > rating[i+1]  => candy[i] > candy[i+1]
#
# Plan:
# 1) Start candies = [1]*n (minimum).
# 2) Left -> Right pass: fix "higher than left neighbor" constraint.
#    If rating[i] > rating[i-1], set candies[i] = candies[i-1] + 1.
# 3) Right -> Left pass: fix "higher than right neighbor" constraint.
#    If rating[i] > rating[i+1], we need candies[i] >= candies[i+1] + 1.
#    Use max(...) so we don't break what pass #2 already set.
# 4) Sum candies.
#
# Complexity: O(n) time (two passes), O(n) space.

#------------- 01(space) soln, notneeded, try to understand--------------------------------------------
    # def candy(self, ratings: List[int]) -> int:
    #     n = len(ratings)
    #     if n == 0:
    #         return 0

    #     total = 1
    #     up = down = peak = 0

    #     for i in range(1, n):
    #         if ratings[i] > ratings[i - 1]:
    #             up += 1
    #             peak = up
    #             down = 0
    #             total += 1 + up
    #         elif ratings[i] == ratings[i - 1]:
    #             up = down = peak = 0
    #             total += 1
    #         else:
    #             up = 0
    #             down += 1
    #             total += 1 + down
    #             if down <= peak:
    #                 total -= 1  # peak already tall enough; avoid double-counting it

    #     return total
#---------------Graph way - bad , slower, O(n) ----------------------------------
        # Graph/DAG view (constraint propagation):
        # - Node i = child i
        # - For each neighbor pair (i, i+1):
        #     if ratings[i] < ratings[i+1]: add edge i -> i+1   (higher rating must get more candies)
        #     if ratings[i] > ratings[i+1]: add edge i+1 -> i
        #     else: no edge (no constraint)
        # - This graph is a DAG because every edge goes from lower rating to higher rating (strictly increasing).
        # - candies[v] = 1 + max(candies[u]) over all incoming edges u -> v
        #   (longest path in DAG), solved via topological order (Kahn's algorithm).


    

