class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index,size) # monotonic increasing
        maxarea = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                ind, size = stack.pop()
                start = ind
                area = (i-ind)*size
                maxarea = max(maxarea,area)

            stack.append((start,heights[i])) #append start ind!!

        #Empty out the stack
        i = len(heights)
        while stack:
            ind,size = stack.pop()
            area = (i-ind)*size
            maxarea = max(area,maxarea)

        return maxarea

#Imp mistake
#I did this --> stack.append((i,heights[i])) but we should have another start index!!
# When you pop a taller bar, you discover: the current smaller height can extend left 
#into the space those taller bars occupied. So the “start index” for the current 
#height is not i; it should become the earliest index among the bars you popped.

#---------------------SOLN IDEA----------------------------------
# Overall: use a monotonic increasing stack so each bar is pushed/popped once.
# When a shorter bar appears, pop taller bars and compute their area using current i as the right boundary.
# Store a start index with each height to know how far left it can extend; carry it leftward while popping.
# Without carrying start, widths get underestimated (e.g., [2,1,2]).

#TIME
# Stack solution time is O(n).
# Reason: each bar index is pushed once and popped once; all 
# while-loops across the run total to at most n pops, so total operations are linear.

##---------othere solns----------------------------------
# 1)Brute force expands each bar left/right to find its max width → O(n²).

#2) Divide-and-conquer splits by the minimum bar and recurses → O(n log n) average, O(n²) worst-case.

# 3)Compute previous/next smaller element arrays with stacks, then area per bar → O(n) (same core idea as your stack solution).


    
        