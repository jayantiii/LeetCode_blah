class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #The key insight to this problem is understanding when we need a new room versus when we can reuse an existing one: #for this we wanna store earliest endtimes, so use min heap!!
        minheap = [] # The heap is supposed to represent meetings currently using rooms.
        conf = 0

        intervals.sort(key = lambda i :i[0]) #sort by start, O(n log n)

        for interval in intervals:
            #To know the smallest element without deleting it, access heap[0]
            if not minheap:
                conf+=1
            else:
                minendtime = minheap[0]
                if minendtime > interval[0]: #if minimum end is more than start
                    conf+=1
                else: 
                    heapq.heappop(minheap) #remove the meeting since it over
            heapq.heappush(minheap, interval[1]) #Heap push/pop per interval O(log n) each

        return conf
        
# Time complexity:
#   - Sorting intervals: O(n log n), total heap work: O(n log n)
#   - Overall: O(n log n) + O(n log n) = O(n log n)

#heap size will be number of active conference rooms
#We can simply check the room which is due to get vacated the earliest amongst all the allocated rooms.

#Dont do this,adding all end times intially to heap, this is just bag of all end times
#if we do this then minendtime is not “earliest end among active meetings but it’s “earliest end among all meetings ever inserted”.

#Deepti soln
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if not intervals:
        #     return 0

        # # Step 1: sort by start time
        # intervals.sort(key=lambda x: x[0])

        # # Step 2: initialize min heap to store current meeting end times
        # heap = []
        # meeting_rooms = 0

        # for start, end in intervals:
        #     # Step 3: if earliest meeting finished before this starts, free a room
        #     if heap and heap[0] <= start:
        #         heapq.heappop(heap)

        #     # Step 4: allocate a room (push current meeting’s end time)
        #     heapq.heappush(heap, end)

        #     # Step 5: track max rooms used at any time
        #     meeting_rooms = max(meeting_rooms, len(heap))

        # return meeting_rooms


#Half Wrong answer!!
# My answer passed 52/79, not the right way, has some flaws
#This doesnt consider that previous conference room can get freed then what
#Falied - [[9,10],[4,9],[4,17]] - sort - [[4,9][4,17][9,10]]

        # conf = 1  
        # intervals.sort(key = lambda i : i[0])
        # for i in range(1, len(intervals)):
        #     #means overlapping, if start is less than end
        #     if max(intervals[i][0], intervals[i-1][0]) < min(intervals[i][1], intervals[i-1][1]):
        #         conf+=1
        # return conf

