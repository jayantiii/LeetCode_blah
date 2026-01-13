class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [] #(dist, index)
        res = []
        for i, p in enumerate(points):
            x,y = p[0],p[1]
            dist = x**2  + y**2
            heapq.heappush(minheap,(dist,i))

        while k > 0:
            dist, i = heapq.heappop(minheap)
            res.append(points[i])
            k-=1

        return res

# can use  heapq.heapify(heap) too!

#----------Better Binary Search Time complexity: O(N)---------------------------------
# Binary search isn’t on the array order here. It’s on the answer value (the distance threshold T).
# Idea: find a distance threshold T such that at least k points have d <= T, but fewer than k have d < T. Then:

# take all points with d < T
# add enough points with d == T to reach k
# This works because distances are monotonic w.r.t. the threshold.
#max (hi): max(x*x + y*y for all points)

#----------------Quickselect apporach----------------------------
# Quickselect (partition like Quicksort, but only recurse into one side)
# Idea: partition points around a pivot distance so that:
# left side = distances < pivot
# right side = distances >= pivot
# Then only continue on the side that contains the k-th element. Finally, points[:k] are the k closest (order arbitrary).

#-------------------Bruteforce---------------------------------------
#Bruetforce Approach: Sort with Custom Comparator, O(N⋅logN)
#Python, on the other hand, uses TimSort, which is a hybrid of MergeSort and InsertionSort and requires O(N) extra space.

#--------------------Using maxheap when we want heap size k-----------------------
# heap = []  # max-heap via (-dist2, x, y)

#         for x, y in points:
#             dist2 = x*x + y*y
#             item = (-dist2, x, y)

#             if len(heap) < k:
#                 heapq.heappush(heap, item)
#             else:
#                 heapq.heappushpop(heap, item)  # keeps k closest

#         return [[x, y] for _, x, y in heap]



        