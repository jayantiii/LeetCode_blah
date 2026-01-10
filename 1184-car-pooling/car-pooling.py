class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # primary: start time (x[0]), tie-break: end time (x[1])
        trips.sort(key=lambda x: (x[1], x[2]))
        minheap = [] #(endtime, numofpass)
        currentpass = 0

        for numpass, start, end in trips:

            #first drop passengers if they need to be
            while minheap and  minheap[0][0] <= start:
                endtime, num = heapq.heappop(minheap)  #trips that end at this time
                currentpass -= num

            #thenpickup the new passengers
            currentpass += numpass
            heapq.heappush(minheap,(end,numpass))
            if currentpass > capacity:
                return False

        return True

#Line sweep soln!!

  # delta[x] = net change in passengers at location x
        # delta = {}

        # for p, s, e in trips:
        #     delta[s] = delta.get(s, 0) + p   # pick up at start
        #     delta[e] = delta.get(e, 0) - p   # drop at end

        # cur = 0
        # # Must process locations in increasing order (the car moves forward)
        # for x in sorted(delta):
        #     cur += delta[x]
        #     if cur > capacity:
        #         return False

        # return True

#TIME
# Heap (your “prev” solution):
# Time: O(n log n) = sort trips O(n log n) + push/pop each trip O(log n)
# Space: O(n) (heap)

# Line sweep (delta map “this” solution):
# Time: O(n log n) = build deltas O(n) + sort unique locations m ≤ 2n so O(m log m)
# Space: O(n) (delta map)
            

            
            

        