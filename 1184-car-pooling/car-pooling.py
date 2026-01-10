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

            

            
            

        