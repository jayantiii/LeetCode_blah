class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        pairs = [] #[(dist,wi,bj)...]
        for i in range(n):
            for j in range(m):
                p1x= workers[i][0]
                p2x = bikes[j][0]

                p1y= workers[i][1]
                p2y = bikes[j][1]

                dist = abs(p1x-p2x) + abs(p1y-p2y)

                pairs.append((dist,i,j))

        pairs.sort() #IMP - sort by distance!!

        res = [0]*n
        barr = [False]*m #if used
        warr = [False]*n #don’t need warr if you use res[w] != -1
        count = 0
        for i in range(len(pairs)):
            d,w,b = pairs[i]
            if barr[b] or warr[w]: #used up either
                continue

            res[w] = b
            barr[b] = True
            warr[w] = True

            count +=1
            if count == n:
                break

        return res


# Idea (greedy + sorting all pairs):
# Compute every possible (distance, worker, bike) pair.

# Sort pairs so the “best” assignment comes first: smallest distance; if tie, use the required indices as tie-breakers.
# Then scan the sorted list and take the first valid pair where that worker is still unassigned and that bike is still unused.
# Because we process pairs in global priority order, the first time we can assign a worker we’re giving them the best available bike under the tie rules.

#----- uSE OF hEAP---------------------------------
# Min-heap over all pairs (streaming the minimum)
# Idea: push all (dist, wi, bj) into a heap; repeatedly pop smallest and assign if valid.
# This is basically “sort” but using a heap; still O(n*m log(n*m)), but you don’t need to hold a separate sorted array.

#-----Why sort and 2 pointer not work------------------
# Two pointers needs a monotone order where moving a pointer can’t skip a better future match; Manhattan worker–bike distances don’t behave monotonically after sorting workers and bikes separately. pairwise Manhattan distances are not monotonic in those sorted orders
# So the globally best pair 
# (d,i,j) can involve items far inside both lists, and a pointer move can silently skip the true next-best assignment.


#RANDOM --SYNTAX TO SORT AND STORE INDICES---
# a = [(v, i) for i, v in enumerate(arr)]   # [(50,0), (10,1), (40,2)]
# a.sort(key=lambda x: x[0])                # sort by val