class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #Greedy and maxheap
        maxheap = [] # (dist)
        final = 0
        for i in range(len(heights)-1): #range

            diff =heights[i] - heights[i+1] #

            if diff >= 0: #none needed
                continue

            #note - diff is negative now so handle accordingly!!

            # FIX: always try bricks first, dont use a if condn here
            heapq.heappush(maxheap, diff)   # diff is negative
            bricks += diff    # FIX: spend bricks (adds negative => subtracts)


            if bricks < 0: #bricks over, look at ladders
                if ladders == 0:
                    return i

                maxdist = heapq.heappop(maxheap)
                ladders-=1

                # confusing - subtract negative => bricks increase
                bricks = bricks -  maxdist   #  bricks -= (-7) = bricks + 7
                

        return len(heights) - 1 # went till end


# Intuition:
# Spend bricks on every uphill jump and remember those jumps in a max-heap.
# If bricks go negative, “retroactively” use a ladder on the largest jump so far (pop heap) to refund bricks.
# This ensures ladders cover the biggest climbs, and bricks pay the smaller ones. 

#  the algorithm works by letting bricks go negative temporarily and then “fixing” it by swapping one past brick-paid jump to a ladder.


#---------------------------------Backtracking-----------------------
# Time: exponential — worst case you branch on every uphill step.
#   O(2^U)
#   where U = count of indices i with heights[i+1] > heights[i] 
# Space: O(n) recursion stack depth.

        # @lru_cache(None)
        # def backtrack(i,b,l):
        #     #reached last building
        #     if i == len(heights) - 1: #last building
        #         return i
            
        #     # if next step is up and we can't pay for it, we stop here
        #     diff =  heights[i] - heights[i+1] 
        #     if b < diff and l ==0 and diff < 0: # condn  b < diff needed
        #         return i

        #     res = i
        #     if heights[i] >= heights[i+1]: #dont need anything
        #         return backtrack(i+1,b,l) #IMP -> return here

        #     #use bricks
        #     brick,ladder = 0,0
        #     if  b - (heights[i+1] - heights[i]) >=0:
        #         brick = backtrack(i+1, b - (heights[i+1] - heights[i]),l)

        #     #use ladders
        #     if l >=1:
        #        ladder = backtrack(i+1,b,l-1)

        #     return max(brick,ladder,res)

        # return backtrack(0,bricks,ladders)

        # backtrack(0)

# #RETURN IS IMP IN BELOW LINES SO THAT IT DONT TRY BRICK AND LADDERS BRANCH -->

#        if heights[i] >= heights[i+1]: #dont need anything
#                 return backtrack(i+1,b,l) #IMP -> return here
        