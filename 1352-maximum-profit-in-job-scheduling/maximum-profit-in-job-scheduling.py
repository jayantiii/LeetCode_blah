class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #top-down DP (recursion + memoization):
        n = len(profit)
        times = [[startTime[i],endTime[i],profit[i]] for i in range(len(profit))]
        times.sort()

        # IMP - bisect needs a sorted list to search on (starts)
        starts = [t[0] for t in times]

        @lru_cache(None)
        def findprofit(i):
            if i == n:
                return 0

            # skip i: previous chosen job stays the same
            skip = findprofit(i+1) 
         
            # take i: only if it doesn't overlap with previous chosen job
            take = 0
            end_i = times[i][1] #find first job with start >= current end, 
            j = bisect.bisect_left(times, [end_i,-1,-1],i+1) #bisect_left(a, x, lo=0, hi=len(a))

            take = findprofit(j) + times[i][2]
            return max(skip,take)     

        return findprofit(0)

       
# Tips:-
# This is very standard take or skip dp problem, but the issue here are the contraints, so try to optimize for them.
# In the recursive dp solution, you can manage to have a single variable only, which will denote the index of currentTask.
# When you do this currentTask, find the index of the first next task whose startingTime >= endingTime of current task.
# The step 3 can be optimized by using Binary Search
# def findprofit(i,previ,prof):,-- no need of profit as parameter

#---------------Exaplin  j = bisect.bisect_left(times, times[],i+1)--------------------
# times is sorted lexicographically: [start, end, profit]
# so comparisons (and bisect) prioritize start first.
# We bisect with key=[end_i, -INF, -INF] to find the first index j where times[j][0] >= end_i
# (the -INF tail forces the leftmost position among equal starts).
#f some jobs start exactly at end_i, you must land on the earliest of them. Otherwise you’d skip valid candidates.

# If you want an equally correct, less “magic” version, use a separate starts list:
# and use, j = bisect_left(starts, end_i, lo=i+1)


#-------------MLE cause dfs takes 2 params-------------------
    # @lru_cache(None)
    #     def findprofit(i,previ):
    #         if i == n:
    #             return 0

    #         # skip i: previous chosen job stays the same
    #         skip = findprofit(i+1,previ) 
         
    #         # take i: only if it doesn't overlap with previous chosen job
    #         take = 0
    #         if previ == -1 or times[previ][1] <= times[i][0]:
    #             take = findprofit(i+1,i) + times[i][2]
    #         return max(skip,take)
            

    #     return findprofit(0,-1)

##-----------------FIX the MLE by using one param----------------
#This gives TLE Though, we dont use previ and try to find the j next index using loop
#Below is the change needed in take block form the MLE code

            # # take i: only if it doesn't overlap with previous chosen job
            # take = 0
            # j = i+1
            # # advance j until we find the first job with start >= end_i
            # while j < n and times[i][1] > times[j][0]: #no equal sign, it will overshoot
            #     j+=1 